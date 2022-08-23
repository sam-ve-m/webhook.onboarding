# PROJECT IMPORTS
from src.domain.enums.ouroinvest_status.enum import OuroInvestStatus
from src.domain.exceptions.exceptions import StatusSentIsNotValid


class CheckIfEnumStatusIsValid:

    @classmethod
    def check_if_enum_is_valid(
            cls, status: str
    ) -> None:

        valid_status = [valid_status.value for valid_status in OuroInvestStatus]

        if status not in valid_status:
            raise StatusSentIsNotValid
