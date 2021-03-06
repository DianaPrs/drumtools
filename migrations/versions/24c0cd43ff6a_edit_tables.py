"""edit tables

Revision ID: 24c0cd43ff6a
Revises: 
Create Date: 2020-03-28 17:39:38.456359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24c0cd43ff6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('date_of_birth', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('note_duration', sa.String(), nullable=True),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tracks_artist_id'), 'tracks', ['artist_id'], unique=False)
    op.create_table('bars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('empty', sa.Boolean(), nullable=True),
    sa.Column('half', sa.Boolean(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bars_track_id'), 'bars', ['track_id'], unique=False)
    op.create_table('lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('sequence', sa.Integer(), nullable=False),
    sa.Column('position_1', sa.Integer(), nullable=False),
    sa.Column('position_2', sa.Integer(), nullable=True),
    sa.Column('position_3', sa.Integer(), nullable=True),
    sa.Column('position_4', sa.Integer(), nullable=True),
    sa.Column('position_5', sa.Integer(), nullable=True),
    sa.Column('position_6', sa.Integer(), nullable=True),
    sa.Column('position_7', sa.Integer(), nullable=True),
    sa.Column('position_8', sa.Integer(), nullable=True),
    sa.Column('accent_1', sa.Boolean(), nullable=True),
    sa.Column('accent_2', sa.Boolean(), nullable=True),
    sa.Column('accent_3', sa.Boolean(), nullable=True),
    sa.Column('accent_4', sa.Boolean(), nullable=True),
    sa.Column('accent_5', sa.Boolean(), nullable=True),
    sa.Column('accent_6', sa.Boolean(), nullable=True),
    sa.Column('accent_7', sa.Boolean(), nullable=True),
    sa.Column('accent_8', sa.Boolean(), nullable=True),
    sa.Column('intro', sa.Boolean(), nullable=True),
    sa.Column('couplet', sa.Boolean(), nullable=True),
    sa.Column('chorus', sa.Boolean(), nullable=True),
    sa.Column('pre_chorus', sa.Boolean(), nullable=True),
    sa.Column('bridge', sa.Boolean(), nullable=True),
    sa.Column('solo', sa.Boolean(), nullable=True),
    sa.Column('coda', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['position_1'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['position_2'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['position_3'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['position_4'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['position_5'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['position_6'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['position_7'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['position_8'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lines_position_1'), 'lines', ['position_1'], unique=False)
    op.create_index(op.f('ix_lines_position_2'), 'lines', ['position_2'], unique=False)
    op.create_index(op.f('ix_lines_position_3'), 'lines', ['position_3'], unique=False)
    op.create_index(op.f('ix_lines_position_4'), 'lines', ['position_4'], unique=False)
    op.create_index(op.f('ix_lines_position_5'), 'lines', ['position_5'], unique=False)
    op.create_index(op.f('ix_lines_position_6'), 'lines', ['position_6'], unique=False)
    op.create_index(op.f('ix_lines_position_7'), 'lines', ['position_7'], unique=False)
    op.create_index(op.f('ix_lines_position_8'), 'lines', ['position_8'], unique=False)
    op.create_index(op.f('ix_lines_track_id'), 'lines', ['track_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_lines_track_id'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_8'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_7'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_6'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_5'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_4'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_3'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_2'), table_name='lines')
    op.drop_index(op.f('ix_lines_position_1'), table_name='lines')
    op.drop_table('lines')
    op.drop_index(op.f('ix_bars_track_id'), table_name='bars')
    op.drop_table('bars')
    op.drop_index(op.f('ix_tracks_artist_id'), table_name='tracks')
    op.drop_table('tracks')
    op.drop_table('artists')
    # ### end Alembic commands ###
