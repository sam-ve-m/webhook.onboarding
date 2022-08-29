# STANDARD IMPORTS
from unittest.mock import patch
import pytest

# THIRD PART IMPORTS
from persephone_client import Persephone

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import NotSentToPersephone
from src.services.persephone.service import SendToPersephone


exchange_account_stub = {"exchange_dict": "1234567"}
cpf_stub = "43426789810"
status_stub = "Em Análise"
unique_id = "635jdhfbmvkhdidif8374654"

stub_response = {
    'cpf': '43426789810',
    'exchange_account': {'exchange_dict': '1234567'},
    'status': 'Em Análise',
    'unique_id': '635jdhfbmvkhdidif8374654'
}


@pytest.mark.asyncio
@patch.object(Persephone, "send_to_persephone", return_value=(True, True))
@patch("func.src.services.persephone.service.config")
async def test_when_sending_right_params_to_register_user_exchange_member_log_then_return_expected(
        mock_config, mock_send_to_persephone
):
    response = await SendToPersephone.register_user_exchange_member_log(
        unique_id=unique_id,
        status=status_stub,
        cpf=cpf_stub,
        exchange_account=exchange_account_stub
    )
    assert response is None


@pytest.mark.asyncio
@patch.object(Persephone, "send_to_persephone", return_value=(False, False))
@patch("func.src.services.persephone.service.config")
async def test_when_send_to_epersephone_is_false_then_raise_not_sent_to_persephone_error(
        mock_config, mock_send_to_persephone
):
    with pytest.raises(NotSentToPersephone):
        await SendToPersephone.register_user_exchange_member_log(
            unique_id=unique_id,
            status=status_stub,
            cpf=cpf_stub,
            exchange_account=exchange_account_stub
        )


@pytest.mark.asyncio
@patch.object(Persephone, "send_to_persephone", return_value=(False, False))
@patch("func.src.services.persephone.service.config")
async def test_when_send_wrong_params_to_send_to_persephone_then_raise_typeerror_error(
        mock_config, mock_send_to_persephone
):
    with pytest.raises(TypeError):
        await SendToPersephone.register_user_exchange_member_log(
            unique_id=unique_id,
            exchange_account=exchange_account_stub
        )
