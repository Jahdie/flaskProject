from admin_panel import db
from db.models.abstract_models import BaseModelAbstract
from sqlalchemy_utils import IPAddressType
import sqlalchemy as sa

procedure_column = db.Table(
    'procedure_column',
    sa.Column('procedure_id', sa.Integer, sa.ForeignKey('db.procedures.id')),
    sa.Column('column_id', sa.Integer, sa.ForeignKey('db.columns.id')),
    schema='db',
)

trigger_column = db.Table(
    'trigger_column',
    sa.Column('trigger_id', sa.Integer, sa.ForeignKey('db.triggers.id')),
    sa.Column('column_id', sa.Integer, sa.ForeignKey('db.columns.id')),
    schema='db',
)

job_column = db.Table(
    'job_column',
    sa.Column('job_id', sa.Integer, sa.ForeignKey('db.jobs.id')),
    sa.Column('column_id', sa.Integer, sa.ForeignKey('db.columns.id')),
    schema='db',
)

job_procedure = db.Table(
    'job_procedure',
    sa.Column('job_id', sa.Integer, sa.ForeignKey('db.jobs.id')),
    sa.Column('procedure_id', sa.Integer, sa.ForeignKey('db.procedures.id')),
    schema='db',
)


class Server(BaseModelAbstract):
    __tablename__ = 'servers'
    __table_args__ = {'schema': 'db'}
    user = sa.Column(sa.String(1000), nullable=False)
    password = sa.Column(sa.String(1000), nullable=False)
    ip = sa.Column(IPAddressType, nullable=False)
    databases = db.relationship('Database', backref='server')
    jobs = db.relationship('Job', backref='server')
    sources = db.relationship('Source', backref='server')

    def __repr__(self):
        return self.name


class Database(BaseModelAbstract):
    __tablename__ = 'databases'
    __table_args__ = {'schema': 'db'}
    server_id = sa.Column(sa.Integer, sa.ForeignKey('db.servers.id'))
    tables = db.relationship('Table', backref='database')
    procedures = db.relationship('Procedure', backref='database')
    sources = db.relationship('Source', backref='database')

    def __repr__(self):
        return self.name


class Table(BaseModelAbstract):
    __tablename__ = 'tables'
    __table_args__ = {'schema': 'db'}
    database_id = sa.Column(sa.Integer, sa.ForeignKey('db.databases.id'))
    triggers = db.relationship('Trigger', backref='table')
    columns = db.relationship('Column', backref='table')
    sources = db.relationship('Source', backref='table')

    def __repr__(self):
        return self.name


class Procedure(BaseModelAbstract):
    __tablename__ = 'procedures'
    __table_args__ = {'schema': 'db'}
    database_id = sa.Column(sa.Integer, sa.ForeignKey('db.databases.id'))
    columns = db.relationship('Column', secondary='db.procedure_column',
                              backref=db.backref('procedures'))
    sources = db.relationship('Source', backref='procedure')

    def __repr__(self):
        return self.name


class Job(BaseModelAbstract):
    __tablename__ = 'jobs'
    __table_args__ = {'schema': 'db'}
    server_id = sa.Column(sa.Integer, sa.ForeignKey('db.servers.id'))
    columns = db.relationship('Column', secondary='db.job_column',
                              backref=db.backref('jobs'))
    procedures = db.relationship('Procedure', secondary='db.job_procedure',
                                 backref=db.backref('jobs'))
    sources = db.relationship('Source', backref='job')

    def __repr__(self):
        return self.name


class Trigger(BaseModelAbstract):
    __tablename__ = 'triggers'
    __table_args__ = {'schema': 'db'}
    table_id = sa.Column(db.Integer, sa.ForeignKey('db.tables.id'))
    columns = db.relationship('Column', secondary='db.trigger_column',
                              backref=db.backref('triggers'))
    sources = db.relationship('Source', backref='trigger')

    def __repr__(self):
        return self.name


class Column(BaseModelAbstract):
    __tablename__ = 'columns'
    __table_args__ = {'schema': 'db'}
    table_id = sa.Column(sa.Integer, sa.ForeignKey('db.tables.id'))
    points = db.relationship('Point', backref='column')
    params = db.relationship('Param', backref='column')
    sources = db.relationship('Source', backref='column')

    def __repr__(self):
        return self.name
