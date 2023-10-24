from icecream import ic
from faker import Faker
from faker_food import FoodProvider

from conf.db_session import create_session
from models.tipos_embalagem import TiposEmbalagem


def insert_tipos_embalagem(nome:str) -> None:
    ic("Inserindo Tipos de Embalagem")

    tc = TiposEmbalagem(nome=nome)

    try:
        with create_session() as session:
            session.add(tc)
            session.commit()
    except Exception as e:
        ic("Erro ao inserir tipos embalagem")
        raise e
    else:
        ic(tc, tc.id_)
        ic("Novo Tipo embalagem insrido")

def mock_insert_tipos_embalagem(amount:int = 10) -> None:
    fk = Faker()

    for _ in range(amount):
        nome = fk.unique.color_name()
        insert_tipos_embalagem(nome=nome)



