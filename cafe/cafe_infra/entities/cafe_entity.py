from sqlalchemy import Column, BigInteger, String

from database import Base


class CafeEntity(Base):

    __tablename__ = "cafes"

    id_: int = Column("id", BigInteger, primary_key=True, autoincrement=False)
    name: str = Column(String(100))
    img: str = Column(String(200))
    banner: str = Column(String(200))