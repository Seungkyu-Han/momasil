import os
from functools import lru_cache
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from snowflake import SnowflakeGenerator

load_dotenv()

SNOWFLAKE_INSTANCE = int(os.getenv("SNOWFLAKE_INSTANCE"))


@lru_cache
def get_snowflake_generator() -> SnowflakeGenerator:
    return SnowflakeGenerator(instance=SNOWFLAKE_INSTANCE)


SnowflakeGeneratorDep = Annotated[SnowflakeGenerator, Depends(get_snowflake_generator)]