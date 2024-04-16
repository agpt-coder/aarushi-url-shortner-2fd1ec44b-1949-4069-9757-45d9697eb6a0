import random
import string

import prisma
import prisma.models
from pydantic import BaseModel


class CreateShortURLResponse(BaseModel):
    """
    Contains the resulting short URL after processing the user's request.
    """

    short_url: str


async def create_short_url(long_url: str) -> CreateShortURLResponse:
    """
    Generates a short URL from a given long URL and stores it in the database using Prisma ORM.

    Args:
        long_url (str): The original, long URL to be shortened.

    Returns:
        CreateShortURLResponse: Contains the resulting short URL after processing the user's request.

    This function generates a short URL alias by creating a random string of characters.
    It checks the uniqueness of the alias in the database to ensure no duplicates.
    On success, it stores the mapping in the database and returns the shortened URL.
    """
    alias_length = 8
    potential_alias = "".join(
        random.choices(string.ascii_letters + string.digits, k=alias_length)
    )
    while (
        await prisma.models.URL.prisma().find_unique(where={"alias": potential_alias})
        is not None
    ):
        potential_alias = "".join(
            random.choices(string.ascii_letters + string.digits, k=alias_length)
        )
    temp_user_id = "temp_user_id"
    await prisma.models.URL.prisma().create(
        data={"originalUrl": long_url, "alias": potential_alias, "userId": temp_user_id}
    )
    short_url = f"http://short.url/{potential_alias}"
    return CreateShortURLResponse(short_url=short_url)
