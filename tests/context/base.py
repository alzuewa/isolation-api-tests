from pydantic import BaseModel

from tests.context.scenario import Scenario


class RequestContext(BaseModel):
    """
    Single context for tests layer.

    Provides support for future expansion with trace_id, additional keys, etc. apart from keys.
    """
    scenario: Scenario


def build_grpc_test_metadata(context: RequestContext) -> list[tuple[str, str]]:
    """
    Translates RequestContext into gRPC metadata.

    Used to pass the context to a transport layer,
    from where it can be read by downstream-integrations and mock-server.
    """
    return [('x-test-scenario', context.scenario)]


def build_http_test_headers(context: RequestContext) -> dict[str, str]:
    """
    Translates RequestContext into HTTP headers.

    `x-test-scenario` header describes which mock model has to be used.
    """
    return {'x-test-scenario': context.scenario}
