"""empty message

Revision ID: 10baab0c5d60
Revises: 
Create Date: 2021-04-12 20:29:09.089292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10baab0c5d60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('bottles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('identifier', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('maker', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bottles')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###