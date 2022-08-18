# STANDARD IMPORTS
from typing import Any
import orjson
import re


class ClientDataRequest:

    def __init__(
            self,
            request_body: dict
    ):
        self.__request_body = request_body

    def get_client_ouroinvest_status(self) -> Any:
        message = self.__request_body.get("mensagem")
        message_to_json = orjson.loads(message)

        status = message_to_json.get("statusCadastro")

        return status

    def get_message_to_json(self) -> Any:
        message_raw = self.__request_body.get("mensagem")
        message = orjson.loads(message_raw)

        return message

    def get_cpf_from_message_without_maskara(self) -> str:
        message = self.get_message_to_json()

        cpf_raw = message.get("inscricao")
        cpf = re.sub("[^0-9]", "", cpf_raw)

        return cpf

    def get_message_and_cpf(self) -> tuple:
        status = self.get_client_ouroinvest_status()

        cpf = self.get_cpf_from_message_without_maskara()

        return status, cpf
