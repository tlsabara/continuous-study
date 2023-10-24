from inserts.aditivos_nutritivos import mock_insert_aditivos_nutritivos
from inserts.sabores import mocked_insert_sabores
from conf.db_session import create_tables


if __name__ == "__main__":
    create_tables(drop_all=True)
    mock_insert_aditivos_nutritivos()
    mocked_insert_sabores()
