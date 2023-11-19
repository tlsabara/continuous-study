from conf.db_session import create_tables
from inserts.aditivos_nutritivos import mock_insert_aditivos_nutritivos
from inserts.revendedores import mock_insert_revendedores
from inserts.sabores import mock_insert_sabores
from inserts.tipos_embalagem import mock_insert_tipos_embalagem
from inserts.tipos_picole import mock_insert_tipos_picole
from inserts.conservantes import mock_insert_conservates
from inserts.ingrdientes import mock_insert_ingredientes
from inserts.lotes import mock_insert_lotes


if __name__ == "__main__":
    create_tables(drop_all=True)
    mock_insert_aditivos_nutritivos()
    mock_insert_sabores()
    mock_insert_tipos_embalagem()
    mock_insert_tipos_picole()
    mock_insert_ingredientes()
    mock_insert_conservates()
    mock_insert_revendedores()
    mock_insert_lotes()

