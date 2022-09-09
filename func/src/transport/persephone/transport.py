# THIRD PARTY IMPORTS
from decouple import config
from etria_logger import Gladsheim
from persephone_client import Persephone

# PROJECT IMPORTS
from src.domain.enums.persephone_queue.enum import PersephoneQueue
from src.domain.exceptions.exceptions import NotSentToPersephone
from src.domain.models.exchange_account.model import ExchangeAccount


class SendToPersephone:

    @classmethod
    async def register_user_exchange_member_log(
            cls,
            unique_id: str,
            exchange_account: ExchangeAccount
    ):
        message = exchange_account.log_schema(unique_id)
        success, sent_status = await Persephone.send_to_persephone(
            topic=config("PERSEPHONE_TOPIC"),
            partition=PersephoneQueue.OUROINVEST_ONBOARDING.value,
            message=message,
            schema_name=config("PERSEPHONE_SCHEMA"),
        )
        if success is False:
            Gladsheim.error(
                message="SendToPersephone::register_user_exchange_member_log::Error on trying to register log",
                status=sent_status,
            )
            raise NotSentToPersephone
