from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserDB(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(254), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    student_id: Mapped[str] = mapped_column(String(8), unique=True, nullable=False)
