"""add Tag table

Revision ID: 23916189a657
Revises: d8cf97a22b9e
Create Date: 2018-05-07 12:56:26.480894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23916189a657'
down_revision = 'd8cf97a22b9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_tags_id'), 'tags', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tags_id'), table_name='tags')
    op.drop_table('tags')
    # ### end Alembic commands ###
