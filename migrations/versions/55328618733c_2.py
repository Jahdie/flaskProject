"""2

Revision ID: 55328618733c
Revises: 
Create Date: 2023-09-07 04:15:53.362071

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '55328618733c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('desktops',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    schema='app'
                    )
    op.create_table('servers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('user', sa.String(length=1000), nullable=False),
                    sa.Column('password', sa.String(length=1000), nullable=False),
                    sa.Column('ip', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    schema='db'
                    )
    op.create_table('formulas',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    schema='pt'
                    )
    op.create_table('tabs',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('desktop_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['desktop_id'], ['app.desktops.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='app'
                    )
    op.create_table('databases',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('server_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['server_id'], ['db.servers.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='db'
                    )
    op.create_table('jobs',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('server_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['server_id'], ['db.servers.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='db'
                    )
    op.create_table('procedures',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('database_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['database_id'], ['db.databases.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='db'
                    )
    op.create_table('tables',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('database_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['database_id'], ['db.databases.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='db'
                    )
    op.create_table('columns',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('table_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['table_id'], ['db.tables.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='db'
                    )
    op.create_table('job_procedure',
                    sa.Column('job_id', sa.Integer(), nullable=True),
                    sa.Column('procedure_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['job_id'], ['db.jobs.id'], ),
                    sa.ForeignKeyConstraint(['procedure_id'], ['db.procedures.id'], ),
                    schema='db'
                    )
    op.create_table('triggers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('table_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['table_id'], ['db.tables.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='db'
                    )
    op.create_table('job_column',
                    sa.Column('job_id', sa.Integer(), nullable=True),
                    sa.Column('column_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['column_id'], ['db.columns.id'], ),
                    sa.ForeignKeyConstraint(['job_id'], ['db.jobs.id'], ),
                    schema='db'
                    )
    op.create_table('procedure_column',
                    sa.Column('procedure_id', sa.Integer(), nullable=True),
                    sa.Column('column_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['column_id'], ['db.columns.id'], ),
                    sa.ForeignKeyConstraint(['procedure_id'], ['db.procedures.id'], ),
                    schema='db'
                    )
    op.create_table('trigger_column',
                    sa.Column('trigger_id', sa.Integer(), nullable=True),
                    sa.Column('column_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['column_id'], ['db.columns.id'], ),
                    sa.ForeignKeyConstraint(['trigger_id'], ['db.triggers.id'], ),
                    schema='db'
                    )
    op.create_table('points',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('is_column', sa.Boolean(), nullable=True),
                    sa.Column('column_id', sa.Integer(), nullable=True),
                    sa.Column('tab_id', sa.Integer(), nullable=True),
                    sa.Column('formula_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['column_id'], ['db.columns.id'], ),
                    sa.ForeignKeyConstraint(['formula_id'], ['pt.formulas.id'], ),
                    sa.ForeignKeyConstraint(['tab_id'], ['app.tabs.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='pt'
                    )
    op.create_table('sources',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('server_id', sa.Integer(), nullable=True),
                    sa.Column('database_id', sa.Integer(), nullable=True),
                    sa.Column('table_id', sa.Integer(), nullable=True),
                    sa.Column('column_id', sa.Integer(), nullable=True),
                    sa.Column('procedure_id', sa.Integer(), nullable=True),
                    sa.Column('trigger_id', sa.Integer(), nullable=True),
                    sa.Column('job_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['column_id'], ['db.columns.id'], ),
                    sa.ForeignKeyConstraint(['database_id'], ['db.databases.id'], ),
                    sa.ForeignKeyConstraint(['job_id'], ['db.jobs.id'], ),
                    sa.ForeignKeyConstraint(['procedure_id'], ['db.procedures.id'], ),
                    sa.ForeignKeyConstraint(['server_id'], ['db.servers.id'], ),
                    sa.ForeignKeyConstraint(['table_id'], ['db.tables.id'], ),
                    sa.ForeignKeyConstraint(['trigger_id'], ['db.triggers.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='pt'
                    )
    op.create_table('formula_source',
                    sa.Column('formula_id', sa.Integer(), nullable=True),
                    sa.Column('source_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['formula_id'], ['pt.formulas.id'], ),
                    sa.ForeignKeyConstraint(['source_id'], ['pt.sources.id'], ),
                    schema='pt'
                    )
    op.create_table('params',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('is_column', sa.Boolean(), nullable=True),
                    sa.Column('column_id', sa.Integer(), nullable=True),
                    sa.Column('point_id', sa.Integer(), nullable=True),
                    sa.Column('formula_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['column_id'], ['db.columns.id'], ),
                    sa.ForeignKeyConstraint(['formula_id'], ['pt.formulas.id'], ),
                    sa.ForeignKeyConstraint(['point_id'], ['pt.points.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='pt'
                    )
    op.create_table('point_source',
                    sa.Column('point_id', sa.Integer(), nullable=True),
                    sa.Column('source_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['point_id'], ['pt.points.id'], ),
                    sa.ForeignKeyConstraint(['source_id'], ['pt.sources.id'], ),
                    schema='pt'
                    )
    op.create_table('param_source',
                    sa.Column('param_id', sa.Integer(), nullable=True),
                    sa.Column('source_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['param_id'], ['pt.params.id'], ),
                    sa.ForeignKeyConstraint(['source_id'], ['pt.sources.id'], ),
                    schema='pt'
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('param_source', schema='pt')
    op.drop_table('point_source', schema='pt')
    op.drop_table('params', schema='pt')
    op.drop_table('formula_source', schema='pt')
    op.drop_table('sources', schema='pt')
    op.drop_table('points', schema='pt')
    op.drop_table('trigger_column', schema='db')
    op.drop_table('procedure_column', schema='db')
    op.drop_table('job_column', schema='db')
    op.drop_table('triggers', schema='db')
    op.drop_table('job_procedure', schema='db')
    op.drop_table('columns', schema='db')
    op.drop_table('tables', schema='db')
    op.drop_table('procedures', schema='db')
    op.drop_table('jobs', schema='db')
    op.drop_table('databases', schema='db')
    op.drop_table('tabs', schema='app')
    op.drop_table('formulas', schema='pt')
    op.drop_table('servers', schema='db')
    op.drop_table('desktops', schema='app')
    # ### end Alembic commands ###
