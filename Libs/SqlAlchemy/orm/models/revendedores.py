import sqlalchemy as sa
from datetime import datetime
from models.utils import ModelBase


class Revendedores(ModelBase):
    __tablename__ = "revendedores"

    id_: int = sa.Column(
        sa.BigInteger().with_variant(sa.Integer, "sqlite"), index=True, primary_key=True, autoincrement=True
    )
    cnpj: str = sa.Column(sa.String(14), unique=True, nullable=False)
    razao_social: str = sa.Column(sa.String(100), unique=False, nullable=False)
    contato: str = sa.Column(sa.String(100), unique=False, nullable=True)
    data_criacao: datetime = sa.Column(
        sa.DateTime, default=datetime.now, nullable=False
    )

    def __repr__(self):
        return f"<Revendedores: {self.razao_social} - {self.cnpj}>"
