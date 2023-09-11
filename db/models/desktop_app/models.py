import sqlalchemy as sa

from db.models.abstract_models import BaseModelAbstract
from admin_panel import db


class Desktop(BaseModelAbstract):
    __tablename__ = 'desktops'
    __table_args__ = {'schema': 'app'}
    tabs = db.relationship('Tab', backref='desktop')

    def __repr__(self):
        return self.name

class Tab(BaseModelAbstract):
    __tablename__ = 'tabs'
    __table_args__ = {'schema': 'app'}
    desktop_id = sa.Column(sa.Integer, sa.ForeignKey('app.desktops.id'))
    points = db.relationship('Point', backref='tab')

    def __repr__(self):
        return self.name
