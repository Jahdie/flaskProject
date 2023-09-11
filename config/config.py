from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных
    db_driver: str  # драйвер ДБ
    db_dialect: str  # диалект базы данных


@dataclass
class Config:
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        db=DatabaseConfig(
            database=env("DATABASE"),
            db_host=env("DB_HOST"),
            db_user=env("DB_USER"),
            db_password=env("DB_PASSWORD"),
            db_driver=env("DB_DRIVER"),
            db_dialect=env("DB_DIALECT"),
        )
    )
    # Инициализируем конфиг


config: Config = load_config()
