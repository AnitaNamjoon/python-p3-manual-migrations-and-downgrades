"""Renaming students to scholars

Revision ID: 3d6f4d674af9
Revises: 791279dd0760
Create Date: 2023-09-04 15:25:11.297044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d6f4d674af9'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
