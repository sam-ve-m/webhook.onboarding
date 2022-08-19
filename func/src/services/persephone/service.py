# THIRD PARTY IMPORTS
from decouple import config
from etria_logger import Gladsheim
from persephone_client import Persephone

# PROJECT IMPORTS



# Persephone
# unique_id, status, exchange_account, cpf
# topico - sphinx-persephone.user.crud
# 1.5.0
from func.src.domain.exceptions.exceptions import NotSentToPersephone


class SendToPersephone:

    @classmethod
    async def register_user_exchange_member_log(
            cls,
            unique_id: str,
            status: str,
            cpf: str,
            exchange_account: dict
    ):

        (
            sent_to_persephone,
            status_sent_to_persephone,
        ) = await Persephone.send_to_persephone(
            topic="sphinx-persephone.user.crud",
            partition=0,
            message=ExchangeMemberToPersephone.exchange_member_schema(
                unique_id=unique_id,
                status=status,
                cpf=cpf,
                exchange_account=exchange_account
            ),
            schema_name="to_be_informed",
        )
        if sent_to_persephone is False:
            Gladsheim.error(
                message="SendToPersephone::register_user_exchange_member_log::Error on trying to register log")
            raise NotSentToPersephone
