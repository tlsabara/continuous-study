from icecream import ic
from faker import Faker
from faker_food import FoodProvider

from conf.db_session import create_session
from models.tipos_picole import TiposPicole

def insert_tipos_picole(nome: str) -> None:
    ic("Inserindo tipos picole")
    tp = TiposPicole(nome=nome)

    try:
        with create_session() as session:
            session.add(tp)
            session.commit()
    except Exception as e:
        ic("Erro")
        raise e
    else:
        ic(tp, tp.id_)
        ic("Inserido tipo picole")

def mock_insert_tipos_picole(amount: int = 10) -> None:
    fk = Faker()

    for _ in range(amount):
        nome = fk.unique.company()
        insert_tipos_picole(nome=nome)

