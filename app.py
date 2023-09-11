from flask import redirect
from admin_panel.settings import BaseConfig
from admin_panel import create_app

app = create_app(BaseConfig)


@app.route("/")
def main():
    return redirect("/admin", 302)


# @app.route('/uploads/<path:filename>')
# def download(filename):
#     uploads = DOWNLOAD_FOLDER
#     return send_from_directory(directory=uploads, path=filename)
#

# app.add_url_rule("/import/<model_name>", view_func=ImportView.as_view(name="import"))

if __name__ == "__main__":
    with app.app_context():
        print(app.config)
        app.run()
