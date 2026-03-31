from pydantic import BaseModel, HttpUrl


class HTTPClientTestConfig(BaseModel):
    """
    HTTP-client config in test environment.
    Used by all the test HTTP-clients.
    """

    url: HttpUrl
    timeout: float = 120.0
