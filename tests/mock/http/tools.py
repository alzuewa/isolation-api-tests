from typing import Annotated

from fastapi import Header, HTTPException, status

from tests.context.scenario import Scenario


def get_scenario_http(
    scenario: Annotated[Scenario | None, Header(alias='X-Test-Scenario')] = None
) -> Scenario:
    """
    Extract scenario from obtained request header `X-Test-Scenario` and return it to the caller
    to be used as a key for choosing mock-service behavior and response data.
    """

    # `Annotated` allows to get a value from `Header` param and convert it to `Scenario` enum.
    if not scenario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='X-Test-Scenario header is required',
        )
    return scenario
