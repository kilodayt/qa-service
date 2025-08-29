import sqlalchemy as sa
from alembic import op

revision = "20250827_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_table(
        "answers",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "question_id",
            sa.Integer,
            sa.ForeignKey("questions.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("user_id", sa.String(length=64), nullable=False, index=True),
        sa.Column("text", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )


def downgrade():
    op.drop_table("answers")
    op.drop_table("questions")
