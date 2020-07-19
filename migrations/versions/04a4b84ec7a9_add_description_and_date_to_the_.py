"""Add description and date to the subreddit

Revision ID: 04a4b84ec7a9
Revises: fb97203d1898
Create Date: 2020-07-19 17:37:13.030678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04a4b84ec7a9'
down_revision = 'fb97203d1898'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subreddit', sa.Column('date_created', sa.String(), nullable=True))
    op.add_column('subreddit', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subreddit', 'description')
    op.drop_column('subreddit', 'date_created')
    # ### end Alembic commands ###