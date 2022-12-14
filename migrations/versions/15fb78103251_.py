"""empty message

Revision ID: 15fb78103251
Revises: 
Create Date: 2022-11-21 15:47:02.606415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15fb78103251'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publishing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_publishing_id'), 'publishing', ['id'], unique=False)
    op.create_table('reader',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('telephone', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reader_id'), 'reader', ['id'], unique=False)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('publishing_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publishing_id'], ['publishing.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
    op.create_table('giving',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('mark', sa.String(), nullable=True),
    sa.Column('reader_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['reader_id'], ['reader.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_giving_id'), 'giving', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_giving_id'), table_name='giving')
    op.drop_table('giving')
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_reader_id'), table_name='reader')
    op.drop_table('reader')
    op.drop_index(op.f('ix_publishing_id'), table_name='publishing')
    op.drop_table('publishing')
    # ### end Alembic commands ###
