# STANDARD IMPORTS
import pytest

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import StatusSentIsNotValid
from src.domain.validator.status_ouroinvest.validator import CheckIfEnumStatusIsValid


def test_when_sending_a_correct_enum_to_check_if_enum_is_valid_then_return_the_expected():
    response = CheckIfEnumStatusIsValid.check_if_enum_is_valid(
        status="Em Análise"
    )
    assert response is None


def test_when_sending_an_incorrect_enum_to_check_if_enum_is_valid_then_raise_expected():
    with pytest.raises(StatusSentIsNotValid):
        CheckIfEnumStatusIsValid.check_if_enum_is_valid(
            status="Em processamento"
        )
