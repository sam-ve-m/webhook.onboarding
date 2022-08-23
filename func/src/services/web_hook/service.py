# PROJECT IMPORTS
from src.domain.exceptions.exceptions import UserWasNotFound
from src.domain.models.web_hook.model import ClientDataRequest
from src.domain.validator.status_ouroinvest.validator import CheckIfEnumStatusIsValid
from src.repositories.user_repository.repositories import UserRepository
from src.services.persephone.service import SendToPersephone
from src.transport.caronte.transport import CaronteTransport


class UpdateOuroInvestInformation:

    @classmethod
    async def update_ouroinvest_exchange_account(
            cls,
            client_data: ClientDataRequest
    ) -> bool:

        status, cpf = client_data.get_message_and_cpf()
        unique_id = await UserRepository.find_client_unique_id(cpf=cpf)

        CheckIfEnumStatusIsValid.check_if_enum_is_valid(status=status)

        exchange_account = await CaronteTransport.get_user_register(
            cpf=cpf
        )

        await SendToPersephone.register_user_exchange_member_log(
            cpf=client_data.get_cpf_from_message_without_maskara(),
            status=client_data.get_client_ouroinvest_status(),
            exchange_account=exchange_account,
            unique_id=unique_id
        )

        was_updated = await UserRepository.update_ouroinvest_user_exchange_account(
            status=status,
            cpf=cpf,
            exchange_account=exchange_account
        )

        if was_updated is False:
            raise UserWasNotFound

        return was_updated
