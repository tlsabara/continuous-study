from datetime import datetime
from random import choice, randint
from typing import Annotated
from pydantic import validate_arguments, Field
from faker import Faker
from icecream import ic

from conf.db_session import create_session
from models.notas_fiscais import NotasFiscais
from models.revendedores import Revendedores

def insert_notas_fiscais(numero_serie:int, valor: float, data: datetime, descricao:str, id_revendedor: int) -> NotasFiscais:
    ic("Inserindo Notas Fiscais")
    ic()
    ic(numero_serie, valor, data, id_revendedor)

    nota = NotasFiscais(valor=valor, data=data, numero_serie=numero_serie,descricao=descricao, id_revendedor=id_revendedor)

    try:
        with create_session() as session:
            session.add(nota)
            session.commit()
    except Exception as e:
        ic("Erro ao inserir Notas Fiscais")
        ic(numero_serie, valor, data, id_revendedor)
        raise e
    else:
        ic("Notas Fiscais inseridas com sucesso")
        ic(nota, nota.id_)
        ic()
        return nota


@validate_arguments
def mock_insert_notas_fiscais(amount: Annotated[int, Field(ge=10, lt=1000)] = 10) -> None:
    ic()
    fkr = Faker(["pt_BR"])

    try:
        with create_session() as session:
            list_revendedores = session.query(Revendedores).all()
    except Exception as e:
        ic("Erro")
        ic(e)
        return

    for _ in range(amount):
        cnpj = fkr.unique.company_id()
        valor = randint(10000, 1000000) / randint(10, 10000)
        data = fkr.date_time()
        descricao = fkr.paragraph(nb_sentences=1)
        id_revendedor = choice(list_revendedores)

        insert_notas_fiscais(numero_serie=cnpj, valor=valor, data=data, id_revendedor=id_revendedor.id_, descricao=descricao)