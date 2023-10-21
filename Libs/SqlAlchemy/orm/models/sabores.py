import sqlalchemy as sa
from datetime import datetime

from models.utils import ModelBase


class Sabores(ModelBase):
    __tablename__ = "sabores"

    id_: int = sa.Column(
        sa.BigInteger, autoincrement=True, primary_key=True, index=True
    )
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
    nome: str = sa.Column(sa.String(45), nullable=False, unique=True)

    def __repr__(self):
        return f"<Sabores: {self.nome}>"
