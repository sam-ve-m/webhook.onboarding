import pytest
from decouple import Config
from unittest.mock import patch, MagicMock

from caronte import AllowedHTTPMethods, ExchangeCompanyApi

from src.transport.caronte.transport import CaronteTransport
from src.domain.exceptions.exceptions import CaronteTransportError
from src.domain.models.exchange_account.model import ExchangeAccount


dummy_cpf = "dummy cpf"
dummy_status = "dummy status"
stub_message = MagicMock(cpf=dummy_cpf, status=dummy_status)

success_none = None, True
content_none = True, None


@pytest.mark.asyncio
@pytest.mark.parametrize("dummy_success,dummy_content", [success_none, content_none])
@patch.object(Config, "__call__", return_value="{}")
@patch.object(ExchangeCompanyApi, "request_as_company")
@patch.object(ExchangeAccount, "from_request")
async def test_get_exchange_account_raising_error(
        mocked_model, mocked_transport, mocked_env,
        dummy_success, dummy_content,
):
    mocked_transport.return_value = dummy_success, None, dummy_content
    with pytest.raises(CaronteTransportError):
        await CaronteTransport.get_exchange_account(stub_message)
    mocked_transport.assert_called_once_with(method=AllowedHTTPMethods.GET, url=dummy_cpf)
    mocked_model.assert_not_called()
    mocked_env.assert_called()


@pytest.mark.asyncio
@patch.object(Config, "__call__", return_value="{}")
@patch.object(ExchangeCompanyApi, "request_as_company")
@patch.object(ExchangeAccount, "from_request")
async def test_get_exchange_account(mocked_model, mocked_transport, mocked_env):
    expected_response, dummy_content = "response", "dummy_content"
    mocked_transport.return_value = True, None, dummy_content
    mocked_model.return_value = expected_response
    response = await CaronteTransport.get_exchange_account(stub_message)
    mocked_transport.assert_called_once_with(method=AllowedHTTPMethods.GET, url=dummy_cpf)
    mocked_model.assert_called_once_with(raw_account=dummy_content, cpf=dummy_cpf, status=dummy_status)
    mocked_env.assert_called()
    assert response == expected_response
