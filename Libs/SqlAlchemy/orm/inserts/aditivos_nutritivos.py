from icecream import ic
from faker import Faker
from faker_food import FoodProvider

from conf.db_session import create_session
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
        ic(an, an.id_)
        ic("Novo Aditivos Nutritivos cadastrado com sucesso.")


def mock_insert_aditivos_nutritivos(amont: int = 10) -> None:
    mocker = Faker(["pt_BR"])
    mocker.add_provider(FoodProvider)

    for _ in range(amont):
        nome = mocker.unique.ingredient()
        formula_quimica = mocker.unique.ripe_id()

        insert_adtivos_nutritivos(nome=nome, formula_quimica=formula_quimica)