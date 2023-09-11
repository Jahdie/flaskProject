from admin_panel import db
import sqlalchemy as sa


class BaseModelAbstract(db.Model):
    __abstract__ = True
    id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(1000), nullable=False)
    description = sa.Column(sa.Text(), nullable=True)
