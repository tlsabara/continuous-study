from faker import Faker
from faker_food import FoodProvider
from icecream import ic
from typing import Annotated
from pydantic import validate_arguments, Field

from conf.db_session import create_session
from models.ingredientes import Ingrdientes


def insert_ingrdientes(nome: str) -> Ingrdientes:
    ic(f"Inserindo Ingredientes")
    ic(nome)

    ingrediente = Ingrdientes(nome=nome)
    try:
        with create_session() as session:
            session.add(ingrediente)
            session.commit()
    except Exception as e:
        ic("Erro ao inserir Ingredientes")
        ic(nome)
        raise e
    else:
        ic("Ingrediente inserido com sucesso")
        ic(ingrediente, ingrediente.id_)
        return ingrediente


@validate_arguments
def mock_insert_ingredientes(amount: Annotated[int, Field(ge=10, lt=1000)] = 10) -> None:
    ic()
    fkr = Faker()
    fkr.add_provider(FoodProvider)

    for _ in range(amount):
        name = fkr.unique.ingredient()
        insert_ingrdientes(nome=name)