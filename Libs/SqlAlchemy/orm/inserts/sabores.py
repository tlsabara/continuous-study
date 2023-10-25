from icecream import ic
from faker import Faker
from faker_food import FoodProvider
from typing import Annotated
from pydantic import validate_arguments, Field

from conf.db_session import create_session
from models.sabores import Sabores

def insert_sabores(nome:str) -> Sabores:
    ic("Inserindo Sabores")

    sabor = Sabores(nome=nome)

    try:
        with create_session() as session:
            session.add(sabor)
            session.commit()
    except Exception as e:
        ic(e)
        raise e
    else:
        ic(sabor, sabor.id_)
        ic("Sabor inserido com sucesso")
        return sabor


@validate_arguments
def mock_insert_sabores(amount: Annotated[int, Field(ge=10, lt=1000)] = 10) -> None:
    ic()
    fkr = Faker(["pt_BR"])
    fkr.add_provider(FoodProvider)

    for _ in range(amount):
        name = fkr.unique.fruit()
        insert_sabores(nome=name)
