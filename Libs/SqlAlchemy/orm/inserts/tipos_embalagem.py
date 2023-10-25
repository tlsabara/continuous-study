from icecream import ic
from faker import Faker
from typing import Annotated
from pydantic import validate_arguments, Field


from conf.db_session import create_session
from models.tipos_embalagem import TiposEmbalagem


def insert_tipos_embalagem(nome:str) -> TiposEmbalagem:
    ic("Inserindo Tipos de Embalagem")

    embalagem = TiposEmbalagem(nome=nome)

    try:
        with create_session() as session:
            session.add(embalagem)
            session.commit()
    except Exception as e:
        ic("Erro ao inserir tipos embalagem")
        raise e
    else:
        ic(embalagem, embalagem.id_)
        ic("Novo Tipo embalagem insrido")
        return embalagem


@validate_arguments
def mock_insert_tipos_embalagem(amount: Annotated[int, Field(ge=10, lt=1000)] = 10) -> None:
    ic()
    fkr = Faker()

    for _ in range(amount):
        nome = fkr.unique.color_name()
        insert_tipos_embalagem(nome=nome)



