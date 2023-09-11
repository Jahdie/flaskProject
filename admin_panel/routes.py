from flask_admin import expose, AdminIndexView


class MyMainView(AdminIndexView):
    @expose("/")
    def admin_main(self):
        return self.render("admin/index.html")

