# PROJECT IMPORTS
from func.src.domain.models.web_hook.model import ClientDataRequest
from func.src.domain.validator.status_ouroinvest.validator import CheckIfEnumStatusIsValid
from func.src.repositories.user_repository.repositories import UserRepository
from func.src.transport.caronte.transport import CaronteTransport


class UpdateOuroInvestInformation:

    @classmethod
    async def update_ouroinvest_exchange_account(
            cls,
            client_data: ClientDataRequest
    ) -> bool:

        status, cpf = client_data.get_message_and_cpf()

        CheckIfEnumStatusIsValid.check_if_enum_is_valid(status=status)

        exchange_account = await CaronteTransport.get_user_register(
            cpf=cpf
        )

        was_updated = await UserRepository.update_ouroinvest_user_exchange_account(
            status=status,
            cpf=cpf,
            exchange_account=exchange_account
        )

        # Todo - cobrar Marcão sobre o log no Iara

        return was_updated
