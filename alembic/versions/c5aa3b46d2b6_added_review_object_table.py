"""Added review object table

Revision ID: c5aa3b46d2b6
Revises: 8100476e4caf
Create Date: 2023-12-19 14:38:41.804766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5aa3b46d2b6'
down_revision: Union[str, None] = '8100476e4caf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customers', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'customers', 'restaurants', ['restaurant_id'], ['id'])
    # ### end Alembic commands ###
