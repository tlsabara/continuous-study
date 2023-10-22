import random

from conf.db_session import create_session
from icecream import ic
from faker import Faker
from faker_food import FoodProvider
from models.aditivos_nutritivos import AditivosNutritivos


def insert_adtivos_nutritivos(nome: str, formula_quimica: str) -> None:
    ic("Inserindo Aditivos Nutritivos")

    an = AditivosNutritivos(nome=nome, formula_quimica=formula_quimica)

    try:
        with create_session() as session:
            session.add(an)
            session.commit()
    except Exception as e:
        ic(e)
        raise e
    else:
        ic(an)
        ic("Novo Aditivos Nutritivos cadastrado com sucesso.")


def user_insert_adtivos_nutritivos() -> None:
    ic("Coletando dados do usuário para Aditivos Nutritivos")

    nome: str = input("Digite o nome do aditivo")
    formula_quimica: str = input("Digite a formuila quimica do aditivo")

    insert_adtivos_nutritivos(nome=nome, formula_quimica=formula_quimica)


def mocked_data_aditivos_nutritivos(amont: int = 10) -> None:
    mocker = Faker(["pt_BR"])
    mocker.add_provider(FoodProvider)

    for _ in range(amont):
        nome = mocker.ingredient()
        formula_quimica = mocker.ripe_id()

        insert_adtivos_nutritivos(nome=nome, formula_quimica=formula_quimica)


if __name__ == "__main__":
    mocked_data_aditivos_nutritivos()
