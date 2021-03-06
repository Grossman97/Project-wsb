"""deleted url column

Revision ID: fd02d3ded3b5
Revises: d54996925155
Create Date: 2020-04-07 22:55:26.445073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd02d3ded3b5'
down_revision = 'd54996925155'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'translated_file_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('translated_file_url', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
