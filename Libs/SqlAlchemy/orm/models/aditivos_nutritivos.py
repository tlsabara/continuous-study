from datetime import datetime
import sqlalchemy as sa
from models.utils import ModelBase


class AditivosNutritivos(ModelBase):
    __tablename__: str = "aditivos_nutritivos"

    id_: int = sa.Column(
        sa.BigInteger().with_variant(sa.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )
    # uuid: str = sa.Column(
    #    sa.Uuid,
    #    autoincrement=True
    # )
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    formula_quimica: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        # este cara quebra algumas coisas pythonicas ai...
        return f"<AditivosNutritivos: {self.nome}>"
