# STANDARD IMPORTS
from unittest.mock import patch
import pytest
from flask import Flask

# STUB IMPORTS
from func.src.repositories.user_repository.repositories import UserRepository
from func.src.transport.caronte.transport import CaronteTransport
from func.src.services.persephone.service import SendToPersephone
from main import update_onboarding_ouroinvest
from web_hook import web_hook_third_response


@pytest.mark.asyncio
@patch.object(UserRepository, "find_client_unique_id", return_value="2d03cc0c-0f75-4483-ae52-a3fc61626182")
@patch.object(CaronteTransport, "get_user_register", return_value="lalala")
@patch.object(SendToPersephone, "register_user_exchange_member_log", return_value=None)
@patch.object(UserRepository, "update_ouroinvest_user_exchange_account", return_value=True)
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
        response = await update_onboarding_ouroinvest(
            request_body=request
        )
        assert response.status_code == 200


@pytest.mark.asyncio
@patch.object(UserRepository, "find_client_unique_id", return_value="2d03cc0c-0f75-4483-ae52-a3fc61626182")
@patch.object(CaronteTransport, "get_user_register", return_value="lalala")
@patch.object(SendToPersephone, "register_user_exchange_member_log", return_value=None)
@patch.object(UserRepository, "update_ouroinvest_user_exchange_account", return_value=False)
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
        response = await update_onboarding_ouroinvest(
            request_body=request
        )
        assert response.status_code == 500
