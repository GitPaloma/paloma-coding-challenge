"""Add Program and Image tables

Revision ID: 6e1f5ea02024
Revises: 
Create Date: 2021-11-28 02:16:43.559379

"""
from alembic import op
import sqlalchemy as sa

from program import DEFAULT_DESCRIPTION
from image import POSTER_ART_DESCRIPTION


# revision identifiers, used by Alembic.
revision = '6e1f5ea02024'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'program',
        sa.Column(
            'id', sa.BigInteger(), sa.Identity(always=True), nullable=False),
        sa.Column('title', sa.Text(), nullable=False),
        sa.Column(
            'description',
            sa.Text(),
            nullable=False,
            server_default=DEFAULT_DESCRIPTION),
        sa.Column(
            'program_type',
            sa.Enum('movie', 'series', name='programtype'),
            nullable=False),
        sa.Column('release_year', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id'))
    op.create_table(
        'image',
        sa.Column(
            'id', sa.BigInteger(), sa.Identity(always=True), nullable=False),
        sa.Column('program_id', sa.BigInteger(), nullable=False),
        sa.Column(
            'description',
            sa.Text(),
            nullable=False,
            server_default=POSTER_ART_DESCRIPTION),
        sa.Column('height', sa.Integer(), nullable=False),
        sa.Column('width', sa.Integer(), nullable=False),
        sa.Column('url', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['program_id'], ['program.id']),
        sa.PrimaryKeyConstraint('id'))
    op.create_index(
        'one_poster_art_per_program',
        'image',
        ['program_id'],
        unique=True,
        postgresql_where=sa.text("description = 'Poster Art'"))


def downgrade():
    op.drop_table('image')
    op.drop_table('program')
