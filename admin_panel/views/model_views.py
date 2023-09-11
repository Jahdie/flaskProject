from .custom_model_view import CustomModelView
from admin_panel.utils.formatters import name_formatter, backref_formatter


class DesktopModelView(CustomModelView):
    column_list = (
        'id', 'name', 'tabs', 'description',
    )


class TabModelView(CustomModelView):
    column_list = (
        'id', 'name', 'desktop', 'points', 'description',
    )


class ServerModelView(CustomModelView):
    column_list = (
        'id', 'name', 'user', 'password', 'ip', 'databases', 'jobs', 'sources', 'description',
    )


class DatabaseModelView(CustomModelView):
    column_list = (
        'id', 'name', 'server', 'tables', 'procedures', 'sources', 'description',
    )


class TableModelView(CustomModelView):
    column_list = (
        'id', 'name', 'database', 'triggers', 'columns', 'sources', 'description',
    )


class ColumnModelView(CustomModelView):
    column_list = (
        'id', 'name', 'table', 'procedures', 'jobs', 'triggers', 'sources', 'points', 'params', 'description',
    )


class JobModelView(CustomModelView):
    column_list = (
        'id', 'name', 'server', 'columns', 'procedures', 'sources', 'description',
    )


class ProcedureModelView(CustomModelView):
    column_list = (
        'id', 'name', 'database', 'columns', 'jobs', 'sources', 'description',
    )


class TriggerModelView(CustomModelView):
    column_list = ('id', 'name', 'table', 'columns', 'sources', 'description',)


class PointModelView(CustomModelView):
    column_list = ('id', 'name', 'is_column', 'point_num', 'formula', 'tab', 'column', 'params', 'sources', 'description',)
    # form_columns = ('name', 'column_id', 'desktop_id', 'is_column', 'description')
    # column_display_all_relations = True


class ParamModelView(CustomModelView):
    column_list = ('id', 'name', 'is_column', 'point', 'formula', 'column', 'sources', 'description',)


class SourceModelView(CustomModelView):
    column_list = (
        'id', 'name', 'server', 'database', 'table', 'column', 'procedure', 'job', 'triggers', 'points', 'params',
        'description',
    )


class FormulaModelView(CustomModelView):
    column_list = ('id', 'name', 'sources', 'description')
