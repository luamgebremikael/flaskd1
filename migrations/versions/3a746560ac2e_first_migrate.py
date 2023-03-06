"""first migrate

Revision ID: 3a746560ac2e
Revises: 
Create Date: 2023-03-05 23:12:38.105718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a746560ac2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(length=64), nullable=True),
    sa.Column('model', sa.String(length=64), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('datecreated', sa.Integer(), nullable=False),
    sa.Column('User_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'year', 'price', 'datecreated', 'User_id'),
    sa.UniqueConstraint('color'),
    sa.UniqueConstraint('make'),
    sa.UniqueConstraint('model')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('Firstname', sa.String(length=64), nullable=True),
    sa.Column('Lastname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Firstname'),
    sa.UniqueConstraint('Lastname'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('car')
    # ### end Alembic commands ###
