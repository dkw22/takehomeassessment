"""first migration

Revision ID: 39688f001e69
Revises: 
Create Date: 2021-07-27 15:11:47.571843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39688f001e69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('divvy',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.Column('stoptime', sa.DateTime(), nullable=False),
    sa.Column('bikeid', sa.Integer(), nullable=True),
    sa.Column('from_station_id', sa.Integer(), nullable=True),
    sa.Column('from_station_name', sa.String(), nullable=True),
    sa.Column('to_station_id', sa.Integer(), nullable=True),
    sa.Column('usertype', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('trip_duration', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('divvy')
    # ### end Alembic commands ###
