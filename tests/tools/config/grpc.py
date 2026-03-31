from pydantic import BaseModel, IPvAnyAddress


class GRPCServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress

    @property
    def url(self):
        return f'{self.address}:{self.port}'


class GRPCClientTestConfig(BaseModel):
    """
    gRPC-client config in test environment.
    Defines connection params to gRPC-service regardless of specific client.
    """

    port: int
    address: IPvAnyAddress

    @property
    def url(self):
        """
        gRPC-service address, host:port.
        Used at gRPC-channel initialization.
        """
        return f'{self.address}:{self.port}'
