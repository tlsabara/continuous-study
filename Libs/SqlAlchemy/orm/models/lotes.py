import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.utils import ModelBase
from models.tipos_picole import TiposPicole


class Lotes(ModelBase):
    __tablename__ = "lotes"
    tipos_picole: TiposPicole = orm.relationship('TiposPicole', lazy='joined') # Config para o SQLAlchemy

    id_: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True, index=True)
    id_tipo_picole: int = sa.Column(sa.BigInteger, sa.ForeignKey("tipos_picole.id_"), nullable=False)
    quantidade: int = sa.Column(sa.Integer, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
