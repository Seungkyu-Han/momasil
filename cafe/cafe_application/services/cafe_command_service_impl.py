from snowflake import SnowflakeGenerator

from cafe.cafe_core import CafeCommandService, CafeUow, Cafe


class CafeCommandServiceImpl(CafeCommandService):

    def __init__(self, cafe_uow: CafeUow, snowflake_generator: SnowflakeGenerator):
        self.cafe_uow = cafe_uow
        self.snowflake_generator = snowflake_generator

    async def save(self, name: str, img: str, banner: str) -> Cafe:
        cafe: Cafe = Cafe(
            id_=next(self.snowflake_generator),
            name=name,
            img=img,
            banner=banner
        )

        async with self.cafe_uow as uow:
            await uow.cafe_repository.save(cafe=cafe)

        return cafe