"""modulo para criação da engine do ORM que estamos criando

Este módulo comporta as principais features do ORM, que são a criação a engine de conexão, a conexão em si e a
parametrização da engine a ser usada.
"""

import os
from dotenv import load_dotenv
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine

from models.utils import ModelBase
from models import registry

load_dotenv()
__engine: Optional[Engine] = None


def create_engine() -> Engine:
    """Cria uma nova engine de conexão com o banco

    A função foi adaptada para conectar tando a db siglethread como multithread
    """
    global __engine

    if __engine:
        return

    db_url = os.environ.get("DATABASE_URL")
    check_thread = os.environ.get("CHECK_THREAD", "").upper() == "TRUE"
    _args = {"check_same_thread": check_thread}
    __engine = sa.create_engine(url=db_url, echo=False, connect_args=_args)


def create_session() -> Session:
    """Cria uma nova sessão de conexão com o banco de dados"""
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(
        __engine, expire_on_commit=False, class_=Session  # Estudar este parametro.
    )

    return __session()


def create_tables(drop_all: bool = False) -> None:
    """Realiza a criação das tabelas no banco de dados."""
    global __engine

    if not __engine:
        create_engine()
    if drop_all and os.environ.get("STAGE") == "DEV":
        ModelBase.metadata.drop_all(__engine)

    ModelBase.metadata.create_all(__engine)
