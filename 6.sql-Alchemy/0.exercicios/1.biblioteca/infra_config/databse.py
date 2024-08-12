from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from infra_config.configs import AsyncSession




from infra_config.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(
    autoflush = False,
    autocommit = False,
    expire_on_commit = False,
    class_ = AsyncSession,
    bind = engine
)

