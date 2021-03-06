"""Add flair to the data

Revision ID: 042e0e5977cf
Revises: 04a4b84ec7a9
Create Date: 2020-07-25 17:02:29.918925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042e0e5977cf'
down_revision = '04a4b84ec7a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subreddit', sa.Column('flair', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subreddit', 'flair')
    # ### end Alembic commands ###
