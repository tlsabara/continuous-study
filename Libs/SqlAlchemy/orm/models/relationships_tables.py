"""Este arquivo contém todos os relacionamentos de m-n

Definição de todos os relacionamentos muitos para muitos do diagrama es
"""

import sqlalchemy as sa
from datetime import datetime
from models.utils import ModelBase


# Rel: Lotes - NotasFiscais
rel_lotes_nota_fiscal = sa.Table(
    "lotes_nota_fiscal",
    ModelBase.metadata,
    sa.Column("id_notas_fiscais", sa.BigInteger, sa.ForeignKey("notas_fiscais.id_")),
    sa.Column("id_lotes", sa.BigInteger, sa.ForeignKey("lotes.id")),
    sa.Column("data_criacao", sa.DateTime, default=datetime.now, nullable=False),
    sa.Column("active", sa.Boolean, default=True),
)

# Rel: Conservantes - Picole
rel_conservantes_picoles = sa.Table(
    "conservantes_picoles",
    ModelBase.metadata,
    sa.Column("id_conservantes", sa.BigInteger, sa.ForeignKey("conservantes.id_")),
    sa.Column("id_picoles", sa.BigInteger, sa.ForeignKey("picoles.id_")),
    sa.Column("data_criacao", sa.DateTime, default=datetime.now, nullable=False),
    sa.Column("active", sa.Boolean, default=True),
)

# Rel: AtivosNutritivos - Picoles
rel_aditivos_nutritivos_picole = sa.Table(
    "aditivos_nutritivos_picole",
    ModelBase.metadata,
    sa.Column(
        "id_aditivos_nutritivos",
        sa.BigInteger,
        sa.ForeignKey("aditivos_nutritivos.id_"),
    ),
    sa.Column("id_picoles", sa.BigInteger, sa.ForeignKey("picoles.id_")),
    sa.Column("data_criacao", sa.DateTime, default=datetime.now, nullable=False),
    sa.Column("active", sa.Boolean, default=True),
)

# Rel: Ingrdientes - Picole
rel_ingredientes_picole = sa.Table(
    "ingredientes_picole",
    ModelBase.metadata,
    sa.Column("id_ingredientes", sa.BigInteger, sa.ForeignKey("ingredientes.id_")),
    sa.Column("id_picoles", sa.BigInteger, sa.ForeignKey("picoles.id_")),
    sa.Column("data_criacao", sa.DateTime, default=datetime.now, nullable=False),
    sa.Column("active", sa.Boolean, default=True),
)
