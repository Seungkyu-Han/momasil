from typing import Annotated

from fastapi import Depends

from cafe.cafe_application import CafeCommandServiceImpl, CafeQueryServiceImpl
from cafe.cafe_core import CafeCommandService, CafeQueryService
from cafe.cafe_infra_container import CafeRepositoryDep, CafeUowDep
from config.snowflake_generator import SnowflakeGeneratorDep


def get_cafe_query_service(
        cafe_repository: CafeRepositoryDep,
) -> CafeQueryService:
    return CafeQueryServiceImpl(cafe_repository=cafe_repository)

CafeQueryServiceDep = Annotated[CafeQueryService, Depends(get_cafe_query_service)]

def get_cafe_command_service(
        cafe_uow: CafeUowDep,
        snowflake_generator: SnowflakeGeneratorDep
) -> CafeCommandService:
    return CafeCommandServiceImpl(
        cafe_uow=cafe_uow,
        snowflake_generator=snowflake_generator
    )

CafeCommandServiceDep = Annotated[CafeCommandService, Depends(get_cafe_command_service)]

