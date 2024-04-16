import prisma
import prisma.models
from fastapi import HTTPException
from pydantic import BaseModel


class RedirectURLResponse(BaseModel):
    """
    This model represents the response for a redirection request. Ideally, this results in an HTTP 302 redirect response, thus no specific response body is returned to the caller in successful cases.
    """

    location: str


async def redirect_to_long_url(alias: str) -> RedirectURLResponse:
    """
    Redirects from a short URL to the original long URL.

    Args:
        alias (str): The unique alias for the short URL, used to lookup and redirect to the original URL.

    Returns:
        RedirectURLResponse: This model represents the response for a redirection request. Ideally, this results in an HTTP 302 redirect response, thus no specific response body is returned to the caller in successful cases.
    """
    url = await prisma.models.URL.prisma().find_unique(where={"alias": alias})
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectURLResponse(location=url.originalUrl)
