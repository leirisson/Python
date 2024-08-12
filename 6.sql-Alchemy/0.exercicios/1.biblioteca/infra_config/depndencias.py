from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

from infra_config.databse import Session


async def get_session() -> Generator: # type: ignore
    session: AsyncSession = Session()


    try:
        yield session

    finally:
        await session.close()
        