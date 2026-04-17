from logging import Logger

import allure
from httpx import Client, Response, QueryParams, Headers

from tests.clients.http.logger_event_hook import HTTPLoggerEventHook
from tests.context.base import RequestContext, build_http_test_headers
from tests.tools.config.http import HTTPClientTestConfig


class HTTPTestClient:
    """
    Base HTTP API-client.
    """

    def __init__(self, client: Client) -> None:
        self.client = client

    @allure.step('Make GET request to {url}')
    def get(
            self,
            url: str,
            params: QueryParams | None = None,
            context: RequestContext | None = None
    ) -> Response:
        # Headers are created dynamically.
        #
        # If no context passed, request is executed without it 
        # (e.g. for health-checks).
        headers = Headers()

        if context:
            headers = Headers(build_http_test_headers(context))

        return self.client.get(
            url=url,
            params=params,
            headers=headers
        )

def build_http_test_client(
    logger: Logger,
    config: HTTPClientTestConfig
) -> Client:

    logger_event_hook = HTTPLoggerEventHook(logger=logger)

    return Client(
        base_url=str(config.url),
        timeout=config.timeout,
        event_hooks={
            'request': [logger_event_hook.request],
            'response': [logger_event_hook.response],
        },
    )
