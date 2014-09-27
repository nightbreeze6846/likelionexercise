"""empty message

Revision ID: 579a6a542521
Revises: 12d513a0fe61
Create Date: 2014-09-27 14:47:38.658000

"""

# revision identifiers, used by Alembic.
revision = '579a6a542521'
down_revision = '12d513a0fe61'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('content', sa.String(length=255), nullable=True))
    op.add_column('history', sa.Column('endtime', sa.String(length=255), nullable=True))
    op.add_column('history', sa.Column('starttime', sa.String(length=255), nullable=True))
    op.add_column('history', sa.Column('tag', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history', 'tag')
    op.drop_column('history', 'starttime')
    op.drop_column('history', 'endtime')
    op.drop_column('history', 'content')
    ### end Alembic commands ###