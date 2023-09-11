from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.orm import Session, sessionmaker

from config.config import Config


class DBManager:

    def __init__(self, config: Config):
        self._config = config
        self._engine = None
        self._session = None
        self.connection_string = f"{self.config.db.db_dialect}+{self.config.db.db_driver}://" \
                                 f"{self.config.db.db_user}:{self.config.db.db_password}@{config.db.db_host}/" \
                                 f"{self.config.db.database}"

    @property
    def config(self):
        return self._config

    def _create_engine(self) -> engine.Engine:
        self._sync_engine = create_engine(
            self.connection_string,
            echo=False
        )
        return self._engine

    def _is_engine(self) -> None:
        if not self._sync_engine:
            raise ValueError("engin not created")

    def _create_session(self) -> None:
        self._is_engine()
        self._session = sessionmaker(self._engine, expire_on_commit=False)

    @property
    def session(self) -> Session:
        self._create_engine()
        self._create_session()
        with self._session() as session:
            return session


class DAO:

    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager
