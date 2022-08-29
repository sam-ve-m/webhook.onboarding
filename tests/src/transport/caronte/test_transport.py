# STANDARD IMPORTS
from unittest.mock import patch

import pytest
# THIRD PART IMPORTS
from caronte import OuroInvestApiTransport

# PROJECT IMPORTS
from api_response import api_response_stub
from src.domain.exceptions.exceptions import CaronteTransportError
from src.transport.caronte.transport import CaronteTransport


@pytest.mark.asyncio
@patch.object(OuroInvestApiTransport, "execute_get_with_default_token", return_value=api_response_stub)
async def test_when_sending_right_params_to_caronte_transport_then_return_expected(
        mock_execute_get_with_default_token
):
    response = await CaronteTransport.get_user_register(
        cpf="43426789810"
    )
    assert response == api_response_stub


@pytest.mark.asyncio
async def test_when_sending_no_param_right_params_to_caronte_transport_then_raise_error():
    with pytest.raises(CaronteTransportError):
        await CaronteTransport.get_user_register(
            cpf=None
        )
