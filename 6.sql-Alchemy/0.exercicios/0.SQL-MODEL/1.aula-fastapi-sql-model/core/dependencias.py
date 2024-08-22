from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.banco_de_dados import Session

async def get_session() -> Generator: # type: ignore
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
