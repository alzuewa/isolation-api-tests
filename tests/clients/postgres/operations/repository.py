import allure

from tests.clients.postgres.operations.model import OperationsTestModel
from tests.clients.postgres.operations.session import operations_test_session_factory
from tests.clients.postgres.repository import PostgresTestRepository
from tests.tools.fakers import fake
from tests.types.operations import OperationTestType, OperationTestStatus


class OperationsPostgresTestRepository(PostgresTestRepository):

    @allure.step("Create in-progress purchase operation")
    def create_in_progress_purchase_operation(self) -> OperationsTestModel:
        return self.create(
            OperationsTestModel(
                id=fake.uuid(),
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.IN_PROGRESS,
                amount=fake.amount(),
                user_id=fake.uuid(),
                card_id=fake.uuid(),
                category=fake.category(),
                account_id=fake.uuid(),
                created_at=fake.date_time(),
            )
        )

    @allure.step("Create completed purchase operation")
    def create_completed_purchase_operation(self) -> OperationsTestModel:
        return self.create(
            OperationsTestModel(
                id=fake.uuid(),
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.COMPLETED,
                amount=fake.amount(),
                user_id=fake.uuid(),
                card_id=fake.uuid(),
                category=fake.category(),
                account_id=fake.uuid(),
                created_at=fake.date_time(),
            )
        )


def get_operations_postgres_test_repository() -> OperationsPostgresTestRepository:
    return OperationsPostgresTestRepository(
        session_factory=operations_test_session_factory
    )
