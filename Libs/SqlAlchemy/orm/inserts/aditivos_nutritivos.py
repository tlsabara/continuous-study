from typing import Annotated

from icecream import ic
from faker import Faker
from faker_food import FoodProvider
from pydantic import validate_arguments, Field

from conf.db_session import create_session
from models.aditivos_nutritivos import AditivosNutritivos


def insert_adtivos_nutritivos(nome: str, formula_quimica: str) -> AditivosNutritivos:
    ic("Inserindo Aditivos Nutritivos")
    ic(nome, formula_quimica)
    ic()

    adtivo = AditivosNutritivos(nome=nome, formula_quimica=formula_quimica)

    try:
        with create_session() as session:
            session.add(adtivo)
            session.commit()
    except Exception as e:
        ic("Erro ao inserir Aditivo Nutritivo")
        ic(nome, formula_quimica)

        raise e
    else:
        ic("Novo Aditivos Nutritivos cadastrado com sucesso.")
        ic(adtivo, adtivo.id_)
        ic()
        return adtivo


@validate_arguments
def mock_insert_aditivos_nutritivos(amount: Annotated[int, Field(ge=10, lt=1000)] = 10) -> None:
    ic()
    fkr = Faker(["pt_BR"])
    fkr.add_provider(FoodProvider)

    for _ in range(amount):
        nome = fkr.unique.ingredient()
        formula_quimica = fkr.unique.ripe_id()

        insert_adtivos_nutritivos(nome=nome, formula_quimica=formula_quimica)