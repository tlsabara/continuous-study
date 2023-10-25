from icecream import ic
from faker import Faker
from faker_food import FoodProvider

from conf.db_session import create_session
from models.tipos_picole import TiposPicole

def insert_tipos_picole(nome: str) -> TiposPicole:
    ic("Inserindo tipos picole")
    tipo_picole_ = TiposPicole(nome=nome)

    try:
        with create_session() as session:
            session.add(tipo_picole_)
            session.commit()
    except Exception as e:
        ic("Erro")
        raise e
    else:
        ic(tipo_picole_, tipo_picole_.id_)
        ic("Inserido tipo picole")
        return tipo_picole_

def mock_insert_tipos_picole(amount: int = 10) -> None:
    fkr = Faker()

    for _ in range(amount):
        nome = fkr.unique.company()
        insert_tipos_picole(nome=nome)

