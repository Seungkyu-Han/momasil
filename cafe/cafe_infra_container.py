from typing import Annotated

from fastapi import Depends

from cafe.cafe_core import CafeRepository, CafeUow
from cafe.cafe_infra import CafeRepositoryImpl, SqlCafeUow
from database import SessionDep


def get_cafe_repository(session: SessionDep) -> CafeRepository:
    return CafeRepositoryImpl(session=session)


CafeRepositoryDep = Annotated[CafeRepository, Depends(get_cafe_repository)]


def get_cafe_uow(session: SessionDep) -> CafeUow:
    return SqlCafeUow(session=session, cafe_repository_factory=get_cafe_repository)


CafeUowDep = Annotated[CafeUow, Depends(get_cafe_uow)]
