import sqlalchemy as sa
from datetime import datetime

from sqlalchemy.orm import Mapped

from models.utils import ModelBase


class TiposPicole(ModelBase):
    __tablename__ = "tipos_picole"

    id_: int = sa.Column(
        sa.BigInteger().with_variant(sa.Integer, "sqlite"), index=True, primary_key=True, autoincrement=True
    )
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    data_criacao: datetime = sa.Column(
        sa.DateTime, default=datetime.now, nullable=False
    )

    def __repr__(self):
        return f"<TiposPicole: {self.nome}>"
