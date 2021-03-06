"""added url column

Revision ID: d54996925155
Revises: 4a1580053dfe
Create Date: 2020-04-07 21:57:40.309098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd54996925155'
down_revision = '4a1580053dfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('translated_file_url', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'translated_file_url')
    # ### end Alembic commands ###
