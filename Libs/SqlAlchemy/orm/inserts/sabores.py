from icecream import ic
from faker import Faker
from faker_food import FoodProvider

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

def mock_insert_sabores(amount:int = 10) -> None:
    ic()
    fkr = Faker(["pt_BR"])
    fkr.add_provider(FoodProvider)

    for _ in range(amount):
        name = fkr.unique.fruit()
        insert_sabores(nome=name)
