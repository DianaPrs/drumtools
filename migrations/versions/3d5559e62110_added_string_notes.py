"""Added string_notes

Revision ID: 3d5559e62110
Revises: a69c7a768777
Create Date: 2020-04-04 17:55:20.517021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d5559e62110'
down_revision = 'a69c7a768777'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('string_notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bar_id', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('keys', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('accidental', sa.String(), nullable=True),
    sa.Column('dot', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_string_notes_bar_id'), 'string_notes', ['bar_id'], unique=False)
    op.drop_index('ix_string-notes_bar_id', table_name='string-notes')
    op.drop_table('string-notes')
    op.create_foreign_key(None, 'bars', 'tracks', ['track_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.create_foreign_key(None, 'lines', 'bars', ['position_8'], ['id'])
    op.create_foreign_key(None, 'lines', 'bars', ['position_3'], ['id'])
    op.create_foreign_key(None, 'lines', 'bars', ['position_5'], ['id'])
    op.create_foreign_key(None, 'lines', 'bars', ['position_1'], ['id'])
    op.create_foreign_key(None, 'lines', 'bars', ['position_2'], ['id'])
    op.create_foreign_key(None, 'lines', 'bars', ['position_4'], ['id'])
    op.create_foreign_key(None, 'lines', 'bars', ['position_6'], ['id'])
    op.create_foreign_key(None, 'lines', 'bars', ['position_7'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.drop_constraint(None, 'lines', type_='foreignkey')
    op.create_foreign_key(None, 'lines', 'bars', ['position_6'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lines', 'bars', ['position_2'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lines', 'bars', ['position_7'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lines', 'bars', ['position_4'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lines', 'bars', ['position_5'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lines', 'bars', ['position_8'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lines', 'bars', ['position_3'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lines', 'bars', ['position_1'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'bars', type_='foreignkey')
    op.create_table('string-notes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('bar_id', sa.INTEGER(), nullable=True),
    sa.Column('number', sa.INTEGER(), nullable=True),
    sa.Column('keys', sa.VARCHAR(), nullable=True),
    sa.Column('duration', sa.VARCHAR(), nullable=True),
    sa.Column('accidental', sa.VARCHAR(), nullable=True),
    sa.Column('dot', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('dot IN (0, 1)'),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_string-notes_bar_id', 'string-notes', ['bar_id'], unique=False)
    op.drop_index(op.f('ix_string_notes_bar_id'), table_name='string_notes')
    op.drop_table('string_notes')
    # ### end Alembic commands ###