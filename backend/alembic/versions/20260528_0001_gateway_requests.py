"""Create gateway_requests table.

Revision ID: 20260528_0001
Revises: 
Create Date: 2026-05-28 00:32:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = "20260528_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "gateway_requests",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("request_id", sa.String(length=64), nullable=False),
        sa.Column("prompt", sa.Text(), nullable=False),
        sa.Column("model", sa.String(length=100), nullable=False),
        sa.Column("provider", sa.String(length=100), nullable=False),
        sa.Column("response_text", sa.Text(), nullable=True),
        sa.Column("latency_ms", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.create_index(
        "ix_gateway_requests_request_id",
        "gateway_requests",
        ["request_id"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_gateway_requests_request_id", table_name="gateway_requests")
    op.drop_table("gateway_requests")
