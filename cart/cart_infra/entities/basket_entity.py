from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, relationship

from cart.cart_infra.entities.item_entity import ItemEntity
from database import Base


class BasketEntity(Base):

    __tablename__ = "baskets"

    id_: Mapped[int] = Column("id", BigInteger, primary_key=True)
    cafe_id: Mapped[int] = Column(BigInteger, ForeignKey("cafes.id"), nullable=False)
    name: Mapped[str] = Column(String(100))
    item_entities: Mapped[list[ItemEntity]] = relationship(
        "ItemEntity",
        cascade="all, delete-orphan",
        lazy="selectin",
    )