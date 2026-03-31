import logging
from logging import Logger
from pathlib import Path
from typing import TypeVar, Type

import aiofiles
from google.protobuf.json_format import Parse
from google.protobuf.message import Message
from pydantic import BaseModel


HTTPModelT = TypeVar("HTTPModelT", bound=BaseModel)
GRPCModelT = TypeVar("GRPCModelT", bound=Message)


class MockLoader:
    """
    Central mechanism for loading mock-data.

    Responsible for:
    - reading mock JSON-files from disk;
    - logging of loading process;
    - data validation against contracts (Pydantic / Protobuf).
    """

    def __init__(self, root: Path, logger: Logger):
        # Root directory, where mock-files are located.
        self.root = root

        # Pass logger from outside to flexibly set up logging strategy.
        self.logger = logger

    async def get_raw_data(self, file: str) -> str:
        mock_file = self.root / file

        if not mock_file.exists():
            self.logger.error(f'Mock file not found: {mock_file}')
            raise FileNotFoundError(f'Mock file not found: {mock_file}')

        self.logger.info(f'Loading mock file: {mock_file}')

        # Read asynchronously, as it's to be used by async mock-servers.
        async with aiofiles.open(mock_file, mode='r', encoding='utf-8') as async_file:
            return await async_file.read()

    async def load_http(self, file: str, model: Type[HTTPModelT]) -> HTTPModelT:
        raw = await self.get_raw_data(file)

        self.logger.debug(
            f'Validating HTTP mock with Pydantic model: {model.__name__}'
        )

        return model.model_validate_json(raw)

    async def load_grpc(self, file: str, model: Type[GRPCModelT]) -> GRPCModelT:
        raw = await self.get_raw_data(file)

        self.logger.debug(
            f'Validating gRPC mock with Protobuf message: {model.__name__}'
        )

        return Parse(raw, model())
