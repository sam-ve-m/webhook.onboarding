# STANDARD IMPORTS
from unittest.mock import patch
import pytest
from flask import Flask

# STUB IMPORTS
from main import onboarding_ouroinvest
from tests.web_hook import web_hook_third_response

unique_id_stub = "2d03cc0c-0f75-4483-ae52-a3fc61626182"


@pytest.mark.asyncio
@patch("src.repositories.user_repository.repositories.UserRepository.find_client_unique_id",
       return_value=unique_id_stub)
@patch("src.transport.caronte.transport.CaronteTransport.get_user_register", return_value="lalala")
@patch("src.services.persephone.service.SendToPersephone.register_user_exchange_member_log", return_value=None)
@patch(
    "src.repositories.user_repository.repositories.UserRepository.update_ouroinvest_user_exchange_account",
    return_value=True)
async def test_when_sending_right_params_to_update_onboarding_ouroinvest_then_return_the_expected(
        mock_update_ouroinvest_user_exchange_account,
        mock_register_user_exchange_member_log,
        mock_get_user_register,
        mock_find_client_unique_id,
):
    app = Flask(__name__)
    with app.test_request_context(
            json=web_hook_third_response,
    ).request as request:
        response = await onboarding_ouroinvest(
            request_body=request
        )
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("src.repositories.user_repository.repositories.UserRepository.find_client_unique_id",
       return_value=unique_id_stub)
@patch("src.transport.caronte.transport.CaronteTransport.get_user_register", return_value="lalala")
@patch("src.services.persephone.service.SendToPersephone.register_user_exchange_member_log", return_value=None)
@patch(
    "src.repositories.user_repository.repositories.UserRepository.update_ouroinvest_user_exchange_account",
    return_value=False)
async def test_when_sending_right_params_to_update_onboarding_ouroinvest_but_not_updated_on_database(
        mock_update_ouroinvest_user_exchange_account,
        mock_register_user_exchange_member_log,
        mock_get_user_register,
        mock_find_client_unique_id
):
    app = Flask(__name__)
    with app.test_request_context(
            json=web_hook_third_response,
    ).request as request:
        response = await onboarding_ouroinvest(
            request_body=request
        )
        assert response.status_code == 500
