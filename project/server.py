import logging
from contextlib import asynccontextmanager

import project.create_short_url_service
import project.redirect_to_long_url_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="aarushi-url-shortner-2",
    lifespan=lifespan,
    description="To implement a URL shortening service using the specified tech stack (Python, FastAPI, PostgreSQL, and Prisma ORM), the user needs to address several critical components. The service must accept a long URL as an input, generate a uniquely short alias for this URL, store the mapping between the alias and the original URL in a PostgreSQL database using Prisma ORM, and finally, return the shortened URL to the user. When this short URL is accessed, it should redirect the user to the original, long URL. Key considerations from the interview and research include ensuring the uniqueness of the short URL alias by utilizing a mixture of uppercase and lowercase letters, numbers, and possibly employing hash functions, while also avoiding ambiguous characters to prevent confusion. Additionally, the FastAPI framework will handle the redirection through the 'RedirectResponse' class, allowing for a seamless transition to the original URL when the short URL is accessed. Storing the URL mappings requires setting up a model in Prisma that includes at least the original URL and the generated short code, with enhanced functionality such as tracking capabilities as per the user's requirements. This project involves not just the development of a URL shortening functionality but also considerations for security, efficiency, and user experience.",
)


@app.post(
    "/create", response_model=project.create_short_url_service.CreateShortURLResponse
)
async def api_post_create_short_url(
    long_url: str,
) -> project.create_short_url_service.CreateShortURLResponse | Response:
    """
    Generates a short URL from a given long URL.
    """
    try:
        res = await project.create_short_url_service.create_short_url(long_url)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/r/{alias}",
    response_model=project.redirect_to_long_url_service.RedirectURLResponse,
)
async def api_get_redirect_to_long_url(
    alias: str,
) -> project.redirect_to_long_url_service.RedirectURLResponse | Response:
    """
    Redirects from a short URL to the original long URL.
    """
    try:
        res = await project.redirect_to_long_url_service.redirect_to_long_url(alias)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
