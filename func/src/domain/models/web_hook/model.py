# STANDARD IMPORTS
import orjson
import re


class ClientDataRequest:

    def __init__(
            self,
            request_body: dict
    ):
        self.__request_body = request_body

    def get_message_formated(self):
        message = self.__request_body.get("message")
        message_to_json = orjson.loads(message)
        return message_to_json

    def get_cpf_from_message_without_maskara(self):
        message = self.get_message_formated()
        cpf_raw = message.get("inscricao")

        cpf = re.sub("[^0-9]", "", cpf_raw)

        return cpf

    def get_message_and_cpf(self):
        message = self.get_message_formated()
        cpf = self.get_cpf_from_message_without_maskara()

        return message, cpf
