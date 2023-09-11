from flask import Flask
from flask_admin import Admin
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from admin_panel.routes import MyMainView
from flask_migrate import Migrate
from admin_panel.views.model_views import (
    DesktopModelView,
    TabModelView,
    ServerModelView,
    DatabaseModelView,
    TableModelView,
    ProcedureModelView,
    TriggerModelView,
    ColumnModelView,
    JobModelView,
    ParamModelView,
    PointModelView,
    SourceModelView,
    FormulaModelView,
)

babel = Babel()
migrate = Migrate()
db = SQLAlchemy()


def create_app(settings):
    from db.models.desktop_app.models import Desktop, Tab
    from db.models.point.models import Point, Param, Source, Formula
    from db.models.db.models import (
        Server,
        Database,
        Table,
        Procedure,
        Job,
        Trigger,
        Column,
    )
    app = Flask(__name__)
    app.config.from_object(settings)
    babel.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    admin = Admin(app, "Рога и копыта", index_view=MyMainView(), template_mode="bootstrap4", url="/")

    admin.add_view(ServerModelView(Server, db.session))
    admin.add_view(DatabaseModelView(Database, db.session))
    admin.add_view(TableModelView(Table, db.session))
    admin.add_view(ColumnModelView(Column, db.session))
    admin.add_view(TriggerModelView(Trigger, db.session))
    admin.add_view(ProcedureModelView(Procedure, db.session))
    admin.add_view(JobModelView(Job, db.session))
    admin.add_view(PointModelView(Point, db.session))
    admin.add_view(ParamModelView(Param, db.session))
    admin.add_view(SourceModelView(Source, db.session))
    admin.add_view(DesktopModelView(Desktop, db.session))
    admin.add_view(TabModelView(Tab, db.session))
    admin.add_view(FormulaModelView(Formula, db.session))

    return app
