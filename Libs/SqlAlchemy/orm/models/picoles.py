import sqlalchemy as sa
import sqlalchemy.orm as saorm
from datetime import datetime

from sqlalchemy.orm import Mapped

from models.utils import ModelBase
from models.sabores import Sabores
from models.tipos_embalagem import TiposEmbalagem
from models.tipos_picole import TiposPicole
from models.ingredientes import Ingrdientes
from models.conservantes import Conservantes
from models.aditivos_nutritivos import AditivosNutritivos

from models.relationships_tables import (
    rel_conservantes_picoles,
    rel_aditivos_nutritivos_picole,
    rel_ingredientes_picole,
)


class Picoles(ModelBase):
    __tablename__ = "picoles"

    sabores: Mapped[Sabores] = saorm.relationship(
        "Sabores",
        lazy="joined"
    )
    tipos_picole: Mapped[TiposPicole] = saorm.relationship(
        "TiposPicole",
        lazy="joined"
    )
    tipos_embalagem: Mapped[TiposEmbalagem] = saorm.relationship(
        "TiposEmbalagem",
        lazy="joined"
    )
    conservantes_picoles: Mapped[list[Conservantes]] = saorm.relationship(
        "Conservantes",
        secondary=rel_conservantes_picoles,
        backref="conservantes_picoles",
        lazy="joined",
    )
    aditivos_nutritivos_picole: Mapped[list[AditivosNutritivos]] = saorm.relationship(
        "AditivosNutritivos",
        secondary=rel_aditivos_nutritivos_picole,
        backref="aditivos_nutritivos_picole",
        lazy="joined",
    )
    ingredientes_picole: Mapped[list[Ingrdientes]] = saorm.relationship(
        "Ingrdientes",
        secondary=rel_ingredientes_picole,
        backref="ingredientes_picole",
        lazy="joined",
    )

    id_: int = sa.Column(
        sa.BigInteger().with_variant(sa.Integer, "sqlite"),
        index=True,
        autoincrement=True,
        primary_key=True
    )
    preco: float = sa.Column(sa.DECIMAL(8, 2), unique=False)
    data_criacao: datetime = sa.Column(
        sa.DateTime,
        default=datetime.now,
        nullable=False
    )
    id_sabores: int = sa.Column(
        sa.BigInteger,
        sa.ForeignKey("sabores.id_"),
        nullable=False
    )
    id_tipos_embalagem: int = sa.Column(
        sa.BigInteger,
        sa.ForeignKey("tipos_embalagem.id_"),
        nullable=False
    )
    id_tipos_picole: int = sa.Column(
        sa.BigInteger,
        sa.ForeignKey("tipos_picole.id_"),
        nullable=False
    )
