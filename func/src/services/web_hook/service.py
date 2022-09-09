# PROJECT IMPORTS
from src.domain.exceptions.exceptions import UserWasNotFound, UserWasNotUpdated
from src.domain.validator.webhook.validator import WebHookMessage
from src.repositories.user.repository import UserRepository
from src.transport.persephone.transport import SendToPersephone
from src.transport.caronte.transport import CaronteTransport


class ExchangeAccountService:
    @classmethod
    async def save_exchange_account(cls, webhook_message: WebHookMessage) -> bool:
        unique_id = await UserRepository.find_client_unique_id(webhook_message.cpf)
        if not unique_id:
            raise UserWasNotFound

        exchange_account = await CaronteTransport.get_exchange_account(webhook_message)
        await SendToPersephone.register_user_exchange_member_log(
            exchange_account=exchange_account,
            unique_id=unique_id
        )

        was_updated = await UserRepository.update_exchange_account(exchange_account)
        if was_updated is False:
            raise UserWasNotUpdated

        return was_updated
