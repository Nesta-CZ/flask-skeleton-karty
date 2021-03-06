"""empty message

Revision ID: 3d51260d9f81
Revises: 36b93d81ad60
Create Date: 2015-03-04 12:04:51.449655

"""

# revision identifiers, used by Alembic.
revision = '3d51260d9f81'
down_revision = '36b93d81ad60'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loguser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Tomas', sa.String(), nullable=False),
    sa.Column('Michalovsky', sa.String(), nullable=False),
    sa.Column('pohlavi', sa.Boolean(name='muz'), nullable=True),
    sa.Column('datum_insertu', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_loguser'),
    sqlite_autoincrement=True
    )
    op.create_index('ix_loguser_Michalovsky', 'loguser', ['Michalovsky'], unique=False)
    op.create_table('karty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Cislo_Karty', sa.String(), nullable=False),
    sa.Column('Time', sa.DateTime(), nullable=False),
    sa.Column('WTIME', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_karty'),
    sqlite_autoincrement=True
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('karty')
    op.drop_index('ix_loguser_Michalovsky', table_name='loguser')
    op.drop_table('loguser')
    ### end Alembic commands ###
