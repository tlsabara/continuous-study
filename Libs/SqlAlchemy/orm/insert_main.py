from conf.db_session import create_tables
from inserts.aditivos_nutritivos import mock_insert_aditivos_nutritivos
from inserts.sabores import mocked_insert_sabores
from inserts.tipos_embalagem import mock_insert_tipos_embalagem
from inserts.tipos_picole import mock_insert_tipos_picole


if __name__ == "__main__":
    create_tables(drop_all=True)
    mock_insert_aditivos_nutritivos()
    mocked_insert_sabores()
    mock_insert_tipos_embalagem()
    mock_insert_tipos_picole()
