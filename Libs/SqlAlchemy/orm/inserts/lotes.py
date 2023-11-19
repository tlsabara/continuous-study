from faker import Faker
from icecream import ic
from random import choice, randint

from typing import Annotated
from pydantic import validate_arguments, Field

from conf.db_session import create_session
from models.lotes import Lotes
from models.tipos_picole import TiposPicole

def insert_lotes(id_picole: int, quantidade: int) -> Lotes:
    ic(f"Inserindo lote: ")
    ic(id_picole, quantidade)
    lote = Lotes(id_tipo_picole=id_picole, quantidade=quantidade)

    try:
        with create_session() as session:
            session.add(lote)
            session.commit()
    except Exception as e:
        ic(f"Erro ao inserir o lote:")
        ic(id_picole, quantidade)
        raise e
    else:
        ic("Lote inserido com sucesso")
        ic(lote, lote.id_)
        return lote


@validate_arguments
def mock_insert_lotes(amount: Annotated[int, Field(ge=10, lt=1000)] = 10) -> None:
    ic()
    fkr = Faker()

    try:
        with create_session() as session:
            choices_tipo_picole = session.query(TiposPicole).all()
    except Exception as e:
        ic("Erro")
        ic(e)
        return

    for _ in range(amount):
        id_picole = choice(choices_tipo_picole)
        quantidade = randint(20, 10_000)
        insert_lotes(id_picole=id_picole.id_, quantidade=quantidade)
