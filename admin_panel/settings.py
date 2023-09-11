import os
from pathlib import Path

from db.dao import DAO, DBManager
from config.config import config


# db: DAO = DAO(DBManager(config))
# connection_string = db.db_manager.connection_string
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = os.urandom(20)
# DOWNLOAD_FOLDER = BASE_DIR / "files/work/admin/downloads"
# UPLOAD_FOLDER = BASE_DIR / "files/work/admin/uploads"
# ALLOWED_EXTENSIONS = {"csv", "xlsx", "json", }
# FLASK_ADMIN_SWATCH = "sandstone"  # flatly, litera, lumen, sandstone, simplex, solar, yeti
# BABEL_DEFAULT_LOCALE = "ru"
# SQLALCHEMY_DATABASE_URI = connection_string


class BaseConfig:
    SECRET_KEY = os.urandom(20)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_EXTENSIONS = {"csv", "xlsx", "json", }
    FLASK_ADMIN_SWATCH = "sandstone"  # flatly, litera, lumen, sandstone, simplex, solar, yeti
    BABEL_DEFAULT_LOCALE = "ru"
    SQLALCHEMY_DATABASE_URI = f"{config.db.db_dialect}+{config.db.db_driver}://" \
                              f"{config.db.db_user}:{config.db.db_password}@{config.db.db_host}/" \
                              f"{config.db.database}"


