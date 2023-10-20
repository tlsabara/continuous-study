import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.utils import ModelBase
from models.revendedores import Revendedores


class NotasFiscais(ModelBase):
    __tablename__ = "notas_fiscais"
    revendedores: Revendedores = orm.relationship("Revendedores", lazy="joined")

    id_: int = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True, index=True)
    data: datetime = sa.Column(sa.DateTime)
    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    numero_serie: int = sa.Column(sa.Integer,nullable=False, unique=False)
    descricao: str = sa.Column(sa.String(200), nullable=False )
    data_criacao: str = sa.Column(sa.DateTime, default=datetime.now,nullable=False)
    id_revendedor: str = sa.Column(sa.BigInteger, sa.ForeignKey("revendedores.id_"), nullable=False)

    def __repr__(self):
        return f"<NotasFiscais: {self.numero_serie}>"