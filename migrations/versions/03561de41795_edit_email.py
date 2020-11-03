"""edit email

Revision ID: 03561de41795
Revises: 470bded3788c
Create Date: 2020-11-03 12:30:02.510734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03561de41795'
down_revision = '470bded3788c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscribes', sa.Column('email', sa.String(length=100), nullable=True))
    op.drop_constraint('subscribes_emaill_key', 'subscribes', type_='unique')
    op.create_unique_constraint(None, 'subscribes', ['email'])
    op.drop_column('subscribes', 'emaill')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscribes', sa.Column('emaill', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'subscribes', type_='unique')
    op.create_unique_constraint('subscribes_emaill_key', 'subscribes', ['emaill'])
    op.drop_column('subscribes', 'email')
    # ### end Alembic commands ###