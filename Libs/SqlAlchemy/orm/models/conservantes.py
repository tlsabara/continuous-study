import sqlalchemy as sa
from datetime import datetime
from models.utils import ModelBase


class Conservantes(ModelBase):
    __tablename__ = "conservantes"

    id_: int = sa.Column(
        sa.BigInteger().with_variant(sa.Integer, "sqlite"),
        index=True,
        primary_key=True,
        autoincrement=True,
    )
    nome: str = sa.Column(sa.String(45), nullable=False, unique=True)
    descricao: str = sa.Column(sa.String(45), nullable=False, unique=False)
    data_criacao: datetime = sa.Column(
        sa.DateTime, default=datetime.now, nullable=False
    )

    def __repr__(self):
        return f"<Conservantes: {self.nome}>"
