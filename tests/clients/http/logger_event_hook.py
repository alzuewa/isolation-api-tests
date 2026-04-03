from logging import Logger

from httpx import Request, Response


class HTTPLoggerEventHook:
    """
    HTTP-client events handler.

    Used to log requests and responses at a transport layer.
    """

    def __init__(self, logger: Logger):
        self.logger = logger

    def request(self, request: Request):
        # Invoked by httpx before sending HTTP-request.
        self.logger.info(
            f'{request.method} {request.url} - Waiting for response'
        )

    def response(self, response: Response):
        # Invoked by httpx after getting response.
        request = response.request
        self.logger.info(
            f'{request.method} {request.url} - Status {response.status_code}'
        )
