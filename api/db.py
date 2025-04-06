from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from api.settings.settings import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES.user}:{settings.POSTGRES.password}"+\
    f"@{settings.POSTGRES.host}:{settings.POSTGRES.port}/{settings.POSTGRES.dbname}"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session() as session:
        yield session