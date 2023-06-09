"""Initial migration

Revision ID: beec64c9fc8d
Revises: 
Create Date: 2023-03-27 16:51:49.077886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beec64c9fc8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('aula', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'nombre', 'apellido', 'aula')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alumno')
    # ### end Alembic commands ###
