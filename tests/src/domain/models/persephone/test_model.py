# STANDARD IMPORTS
import pytest

# PROJECT IMPORT
from src.domain.models.persephone.model import LogOuroInvestToPersephone

# STUB IMPORTS
from tests.src.domain.models.persephone.file_stub import exchange_account_stub, cpf_stub, status_stub, unique_id, \
    stub_response


def test_when_sending_right_params_to_ouroinvest_schema_message():
    response = LogOuroInvestToPersephone.ouroinvest_schema_message(
        exchange_account=exchange_account_stub,
        cpf=cpf_stub,
        status=status_stub,
        unique_id=unique_id
    )
    assert response == stub_response
    assert isinstance(response, dict)


def test_when_not_sending_right_params_then_raise_error():
    with pytest.raises(TypeError):
        LogOuroInvestToPersephone.ouroinvest_schema_message(
            exchange_account=exchange_account_stub,
            unique_id=unique_id
        )
