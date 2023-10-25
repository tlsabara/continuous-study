from faker_food import FoodProvider
from icecream import ic
from faker import Faker

from models.conservantes import Conservantes
from conf.db_session import create_session


def insert_conservantes(nome: str, descricao: str) -> Conservantes:
    ic(f"Inserindo conservante: ")
    ic(nome)
    conservante = Conservantes(nome=nome, descricao=descricao)

    try:
        with create_session() as session:
            session.add(conservante)
            session.commit()
    except Exception as e:
        ic(f"Erro ao inserir o conservante:")
        ic(nome)
        raise e
    else:
        ic("Conservante inserido com sucesso")
        ic(conservante, conservante.id_)
        return conservante


def mock_insert_conservates(amount: int = 10) -> None:
    ic()
    fkr = Faker()
    fkr.add_provider(FoodProvider)

    for _ in range(amount):
        name = fkr.unique.ingredient()
        description = fkr.unique.paragraph()
        insert_conservantes(nome=name, descricao=description)
