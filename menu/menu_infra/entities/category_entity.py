from sqlalchemy import Column, BigInteger, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped

from database import Base


class CategoryEntity(Base):

    __tablename__ = "categories"

    id_: Mapped[int] = Column("id", BigInteger, primary_key=True)
    name: Mapped[str] = Column(String(100))
    sort_order: Mapped[int] = Column(Integer)
    cafe_id: Mapped[int] = Column(BigInteger, ForeignKey("cafes.id"), nullable=False, index=True)