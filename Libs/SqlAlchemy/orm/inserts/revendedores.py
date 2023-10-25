from faker import Faker
from icecream import ic
from typing import Annotated
from pydantic import validate_arguments, Field

from models.revendedores import Revendedores
from conf.db_session import create_session


def insert_revendedores(cnpj: int, razao_social: str, contato: str) -> Revendedores:
    ic("Inserindo em Revendedores:")
    ic(cnpj, razao_social)
    ic()
    revendedor = Revendedores(cnpj=cnpj, razao_social=razao_social, contato=contato)

    try:
        with create_session() as session:
            session.add(revendedor)
            session.commit()
    except Exception as e:
        ic("Erro em Revendedores:")
        ic(cnpj, razao_social)
        ic()
        raise e
    else:
        ic("Revendedor inserido com sucesso")
        ic(revendedor, revendedor.id_)
        ic()
        return revendedor


@validate_arguments
def mock_insert_revendedores(amount: Annotated[int, Field(ge=10, lt=1000)] = 10) -> None:
    ic()
    fkr = Faker(["pt_BR"])

    for _ in range(amount):
        doc = fkr.unique.company_id()
        company = fkr.unique.neighborhood() + " " +  fkr.company_suffix()
        contact = fkr.name() + " " + fkr.cellphone_number()

        insert_revendedores(cnpj=doc, razao_social=company, contato=contact)