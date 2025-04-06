from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.users import User
from api.core.sec.sec import get_password_hash
import datetime

async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    result = await db.execute(
        select(User)\
            .where(
                User.email == email
            )
        )
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, email: str, password: str, department: str) -> User:
    hashed_password = get_password_hash(password)
    user = User(
        email=email,
        hashed_password=hashed_password,
        department=department,
        created_at=datetime.now()
    )
    await db.add(user)
    await db.commit()
    await db.refresh(user)
    return user