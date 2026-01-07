from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import Mapped

from database import Base


class ItemEntity(Base):

    __tablename__ = "items"

    id_: Mapped[int] = Column("id", BigInteger, primary_key=True)
    menu_id: Mapped[int] = Column(BigInteger, ForeignKey("menus.id"), nullable=False)
    basket_id: Mapped[int] = Column(BigInteger, ForeignKey("baskets.id"), nullable=False, index=True)
    count: Mapped[int] = Column(Integer)