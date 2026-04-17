from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from tests.tools.config.postgres import PostgresClientTestConfig


def get_postgres_test_session_factory(config: PostgresClientTestConfig) -> sessionmaker[Session]:
    """
    sessionmaker factory for tests.

    The only place where:
    - SQLAlchemy engine is created;
    - connection config to Postgres is applied;
    - ORM-sessions behavior in tests is fixed.
    """

    engine = create_engine(
        url=str(config.dsn),

        # manages SQL-queries logging.
        echo=config.echo,

        # switches on '2.0-style' SQLAlchemy behavior to avoid legacy specifics.
        future=True,

        # makes SQLAlchemy check the connection before using it.
        pool_pre_ping=True,
    )

    return sessionmaker(
        bind=engine,
        autoflush=False,

        # forces to use explicit commit for all the changes.
        autocommit=False,

        # prohibits objects "expiration" after the commit was made.
        expire_on_commit=False,
    )