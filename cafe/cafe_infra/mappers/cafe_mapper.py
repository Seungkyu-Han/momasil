from cafe.cafe_core import Cafe
from cafe.cafe_infra.entities.cafe_entity import CafeEntity


def to_domain(cafe_entity: CafeEntity) -> Cafe:
    return Cafe(
        id_=cafe_entity.id_,
        name=cafe_entity.name,
        img=cafe_entity.img,
        banner=cafe_entity.banner,
    )

def to_entity(cafe: Cafe) -> CafeEntity:
    return CafeEntity(
        id_=cafe.id_,
        name=cafe.name,
        img=cafe.img,
        banner=cafe.banner,
    )