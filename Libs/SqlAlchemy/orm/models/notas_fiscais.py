import sqlalchemy as sa
import sqlalchemy.orm as saorm
from datetime import datetime

from sqlalchemy.orm import Mapped

from models.utils import ModelBase
from models.revendedores import Revendedores
from models.lotes import Lotes

from models.relationships_tables import rel_lotes_nota_fiscal


class NotasFiscais(ModelBase):
    __tablename__ = "notas_fiscais"
    revendedores: Mapped[Revendedores] = saorm.relationship(
        "Revendedores", lazy="joined"
    )
    lotes: Mapped[list[Lotes]] = saorm.relationship(
        "Lotes", secondary=rel_lotes_nota_fiscal, backref="lote", lazy="dynamic"
    )

    id_: int = sa.Column(
        sa.BigInteger().with_variant(sa.Integer, "sqlite"), autoincrement=True, primary_key=True, index=True
    )
    data: datetime = sa.Column(sa.DateTime)
    valor: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    numero_serie: int = sa.Column(sa.Integer, nullable=False, unique=False)
    descricao: str = sa.Column(sa.String(200), nullable=False)
    data_criacao: datetime = sa.Column(
        sa.DateTime, default=datetime.now, nullable=False
    )
    id_revendedor: str = sa.Column(
        sa.BigInteger, sa.ForeignKey("revendedores.id_"), nullable=False
    )

    def __repr__(self):
        return f"<NotasFiscais: {self.numero_serie}>"
