"""UserData model added

Revision ID: de269d463c36
Revises: 3d5559e62110
Create Date: 2020-04-05 19:42:32.007395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de269d463c36'
down_revision = 'a830d89d5eaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist', sa.String(255), nullable=False),
    sa.Column('title', sa.String(255), nullable=False),
    sa.Column('comment', sa.String(255), nullable=True),
    sa.Column('notes', sa.String(255), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_data_user_id'), 'user_data', ['user_id'], unique=False)
    # op.drop_index('ix_track_info_user_id', table_name='track_info')
    # op.drop_table('track_info')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_index('ix_string-notes_bar_id', 'string_notes', ['bar_id'], unique=False)
    # op.create_table('track_info',
    # sa.Column('id', sa.INTEGER(), nullable=False),
    # sa.Column('artist', sa.VARCHAR(), nullable=False),
    # sa.Column('title', sa.VARCHAR(), nullable=False),
    # sa.Column('comment', sa.VARCHAR(), nullable=True),
    # sa.Column('notes', sa.VARCHAR(), nullable=False),
    # sa.Column('created', sa.DATETIME(), nullable=False),
    # sa.Column('user_id', sa.INTEGER(), nullable=True),
    # sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_index('ix_track_info_user_id', 'track_info', ['user_id'], unique=False)
    op.drop_index(op.f('ix_user_data_user_id'), table_name='user_data')
    op.drop_table('user_data')
    # ### end Alembic commands ###
