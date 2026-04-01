from grpc import StatusCode
from grpc.aio import ServicerContext

from tests.context.scenario import Scenario


async def get_scenario_grpc(context: ServicerContext) -> Scenario:
    # With gRPC, the scenario is passed via request metadata.

    metadata = dict(context.invocation_metadata())

    raw = metadata.get('x-test-scenario')
    if not raw:
        await context.abort(
            StatusCode.INVALID_ARGUMENT,
            'x-test-scenario metadata is required',
        )

    try:
        return Scenario(raw)
    except ValueError:
        await context.abort(
            StatusCode.INVALID_ARGUMENT,
            f'Unknown test scenario: {raw}',
        )
