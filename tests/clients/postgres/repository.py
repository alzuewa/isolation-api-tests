from contextlib import contextmanager
from typing import Generator, TypeVar

from sqlalchemy.orm import sessionmaker, Session

from tests.clients.postgres.base import BaseTestModel


ModelT = TypeVar('ModelT', bound=BaseTestModel)


class PostgresTestRepository:

    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        # session_factory is passed as a parameter so that repository doesn't create engine on its own
        self.session_factory = session_factory

    @contextmanager
    def session_read(self) -> Generator[Session, None, None]:
        session = self.session_factory()
        try:
            yield session
        finally:
            # close session regardless test result
            session.close()

    @contextmanager
    def session_write(self) -> Generator[Session, None, None]:

        session = self.session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create(self, instance: ModelT) -> ModelT:
        with self.session_write() as session:
            session.add(instance)

            # flush writes all the changes, but does not close the session.
            # allows to get generated fields (id, timestamps) and continue within the same transaction.
            session.flush()
            session.refresh(instance)

        return instance
