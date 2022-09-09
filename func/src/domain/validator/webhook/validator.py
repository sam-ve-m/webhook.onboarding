import re

import orjson
from pydantic import BaseModel, validator

from src.domain.enums.ouroinvest_status.enum import OuroInvestStatus
from src.domain.exceptions.exceptions import StatusSentIsNotValid


class WebHookMessage(BaseModel):
    status: str
    cpf: str

    @validator("status")
    def validate_status(cls, status: str):
        valid_status = [valid_status.value for valid_status in OuroInvestStatus]
        if status not in valid_status:
            raise StatusSentIsNotValid
        return status

    @validator("cpf")
    def unmask_cpf(cls, cpf_raw: str):
        cpf = re.sub("[^0-9]", "", cpf_raw)
        return cpf

    @classmethod
    def from_request(cls, request_body: dict):
        message = orjson.loads(request_body.get("mensagem"))
        status = message.get("statusCadastro")
        cpf = message.get("inscricao")
        return cls(status=status, cpf=cpf)
