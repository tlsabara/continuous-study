from icecream import ic
from faker import Faker
from faker_food import FoodProvider

from conf.db_session import create_session
from models.sabores import Sabores

def insert_sabores(nome:str) -> None:
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

def mocked_insert_sabores(amount:int = 10) -> None:
    mocker = Faker(["pt_BR"])
    mocker.add_provider(FoodProvider)

    for _ in range(amount):
        name = mocker.unique.fruit()
        insert_sabores(nome=name)
