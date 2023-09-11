from itertools import chain
from flask_admin.contrib.sqla import ModelView


class CustomModelView(ModelView):
    column_display_all_relations = True
    column_hide_backrefs = False
    column_display_pk = True
    # column_default_sort = [("deleted_at", True), ("created_at", True), ]
    can_export = True
    export_types = ["csv", "json", "xlsx", ]
    # create_modal = True
    edit_modal = True

    def _export_csv(self, return_url):
        r = super(ModelView, self)._export_csv(return_url)
        r.response = chain((b"\xef\xbb\xbf",), r.response)
        return r

