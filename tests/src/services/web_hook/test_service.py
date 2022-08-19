# STANDARD IMPORTS
from unittest.mock import patch
import pytest

# PROJECT IMPORTS
from func.src.domain.exceptions.exceptions import UserWasNotFound, CaronteTransportError, StatusSentIsNotValid
from func.src.domain.models.web_hook.model import ClientDataRequest
from func.src.repositories.user_repository.repositories import UserRepository
from func.src.services.web_hook.service import UpdateOuroInvestInformation
from func.src.transport.caronte.transport import CaronteTransport

# STUBS
from tests.api_response import api_response_stub
from tests.web_hook import web_hook_fourth_response, web_hook_fourth_response_invalid


@pytest.mark.asyncio
@patch.object(CaronteTransport, "get_user_register", return_value=api_response_stub)
@patch.object(UserRepository, "update_ouroinvest_user_exchange_account", return_value=True)
async def test_when_sending_right_params_to_update_ouroinvest_exchange_account_then_return_the_expected(
        mock_update_ouroinvest_user_exchange_account,
        mock_get_user_register,

):
    response = await UpdateOuroInvestInformation.update_ouroinvest_exchange_account(
        client_data=ClientDataRequest(web_hook_fourth_response)
    )
    assert response is True


@pytest.mark.asyncio
async def test_when_sending_invalid_status_on_requisition_to_exchange_account_then_raise_status_sent_is_not_valid():
    with pytest.raises(StatusSentIsNotValid):
        await UpdateOuroInvestInformation.update_ouroinvest_exchange_account(
            client_data=ClientDataRequest(web_hook_fourth_response_invalid)
        )


@pytest.mark.asyncio
@patch.object(CaronteTransport, "get_user_register", return_value=CaronteTransportError)
async def test_when_caronte_transport_get_user_register_raised_an_error_then_raise_exception(
        mock_get_user_register

):
    with pytest.raises(Exception):
        await UpdateOuroInvestInformation.update_ouroinvest_exchange_account(
            client_data=ClientDataRequest(web_hook_fourth_response)
        )


@pytest.mark.asyncio
@patch.object(CaronteTransport, "get_user_register", return_value=api_response_stub)
@patch.object(UserRepository, "update_ouroinvest_user_exchange_account", return_value=False)
async def test_when_repository_did_not_update_client_data_then_raise_user_not_found_error(
        mock_update_ouroinvest_user_exchange_account,
        mock_get_user_register,

):
    with pytest.raises(UserWasNotFound):
        await UpdateOuroInvestInformation.update_ouroinvest_exchange_account(
            client_data=ClientDataRequest(web_hook_fourth_response)
        )
