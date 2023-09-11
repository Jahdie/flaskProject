import sqlalchemy as sa

from db.models.abstract_models import BaseModelAbstract
from admin_panel import db

point_source = db.Table(
    'point_source',
    sa.Column('point_id', sa.Integer, sa.ForeignKey('pt.points.id')),
    sa.Column('source_id', sa.Integer, sa.ForeignKey('pt.sources.id')),
    schema='pt',
)

param_source = db.Table(
    'param_source',
    sa.Column('param_id', sa.Integer, sa.ForeignKey('pt.params.id')),
    sa.Column('source_id', sa.Integer, sa.ForeignKey('pt.sources.id')),
    schema='pt',
)

formula_source = db.Table(
    'formula_source',
    sa.Column('formula_id', sa.Integer, sa.ForeignKey('pt.formulas.id')),
    sa.Column('source_id', sa.Integer, sa.ForeignKey('pt.sources.id')),
    schema='pt',
)


class Point(BaseModelAbstract):
    __tablename__ = 'points'
    __table_args__ = {'schema': 'pt'}
    point_num = sa.Column(sa.String(1000), nullable=True)
    is_column = sa.Column(sa.Boolean, default=False)
    column_id = sa.Column(sa.Integer, sa.ForeignKey('db.columns.id'))
    tab_id = sa.Column(sa.Integer, sa.ForeignKey('app.tabs.id'))
    formula_id = sa.Column(sa.Integer, sa.ForeignKey('pt.formulas.id'))
    params = db.relationship('Param', backref='point')
    sources = db.relationship('Source', secondary='pt.point_source',
                              backref=db.backref('points'))

    def __repr__(self):
        return self.name


class Param(BaseModelAbstract):
    __tablename__ = 'params'
    __table_args__ = {'schema': 'pt'}
    is_column = sa.Column(sa.Boolean, default=False)
    column_id = sa.Column(sa.Integer, sa.ForeignKey('db.columns.id'))
    point_id = sa.Column(sa.Integer, sa.ForeignKey('pt.points.id'))
    formula_id = sa.Column(sa.Integer, sa.ForeignKey('pt.formulas.id'))
    sources = db.relationship('Source', secondary='pt.param_source',
                              backref=db.backref('params'))

    def __repr__(self):
        return f'{Point.query.filter_by(id=self.point_id).first()}:{self.name}'


class Formula(BaseModelAbstract):
    __tablename__ = 'formulas'
    __table_args__ = {'schema': 'pt'}
    sources = db.relationship('Source', secondary='pt.formula_source',
                              backref=db.backref('formulas'))
    points = db.relationship('Point', backref='formula')
    params = db.relationship('Param', backref='formula')


class Source(BaseModelAbstract):
    __tablename__ = 'sources'
    __table_args__ = {'schema': 'pt'}
    server_id = sa.Column(sa.Integer, sa.ForeignKey('db.servers.id'))
    database_id = sa.Column(sa.Integer, sa.ForeignKey('db.databases.id'))
    table_id = sa.Column(sa.Integer, sa.ForeignKey('db.tables.id'))
    column_id = sa.Column(sa.Integer, sa.ForeignKey('db.columns.id'))
    procedure_id = sa.Column(sa.Integer, sa.ForeignKey('db.procedures.id'))
    trigger_id = sa.Column(sa.Integer, sa.ForeignKey('db.triggers.id'))
    job_id = sa.Column(sa.Integer, sa.ForeignKey('db.jobs.id'))

    def __repr__(self):
        return self.name
