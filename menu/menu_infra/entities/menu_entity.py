from sqlalchemy import Column, BigInteger, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped

from database import Base


class MenuEntity(Base):

    __tablename__ = "menus"

    id_: Mapped[int] = Column("id", BigInteger, primary_key=True)
    category_id: Mapped[int] = Column(BigInteger, ForeignKey("categories.id"), nullable=False, index=True)
    name: Mapped[str] = Column(String(100))
    img: Mapped[str] = Column(String(200))
    sort_order: Mapped[int] = Column(Integer)