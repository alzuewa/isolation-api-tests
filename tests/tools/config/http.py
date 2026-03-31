from pydantic import BaseModel, IPvAnyAddress, HttpUrl


class HTTPServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress


class HTTPClientTestConfig(BaseModel):
    """
    HTTP-client config in test environment.
    Used by all the test HTTP-clients.
    """

    url: HttpUrl
    timeout: float = 120.0
