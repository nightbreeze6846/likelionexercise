"""empty message

Revision ID: 6a8aef0420b
Revises: None
Create Date: 2014-09-15 20:46:57.549000

"""

# revision identifiers, used by Alembic.
revision = '6a8aef0420b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('page_domain', sa.String(length=255), nullable=True),
    sa.Column('subscribe', sa.Integer(), nullable=True),
    sa.Column('join_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###