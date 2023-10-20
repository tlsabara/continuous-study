import sqlalchemy as sa
import sqlalchemy.orm as saorm
from datetime import datetime
from models.utils import ModelBase
from models.sabores import Sabores
from models.tipos_embalagem import TiposEmbalagem
from models.tipos_picole import TiposPicole


class Picoles(ModelBase):
    __tablename__ = "picoles"

    sabores: Sabores = saorm.relationship("Sabores", lazy="joined")
    tipos_picole: TiposPicole = saorm.relationship("TiposPicole", lazy="joined")
    tipos_embalagem: TiposEmbalagem = saorm.relationship("TiposEmbalagem", lazy="joined")