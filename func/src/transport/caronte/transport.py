# STANDARD IMPORTS
from decouple import config

# THIRD PART IMPORTS
from caronte import AllowedHTTPMethods, ExchangeCompanyApi

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import CaronteTransportError
from src.domain.models.exchange_account.model import ExchangeAccount
from src.domain.validator.webhook.validator import WebHookMessage


class CaronteTransport:

    @classmethod
    async def get_exchange_account(cls, message: WebHookMessage) -> ExchangeAccount:
        url = config("OUROINVEST_REGISTER_DATA_URL").format(message.cpf)

        success, request_status, content = await ExchangeCompanyApi.request_as_company(
            method=AllowedHTTPMethods.GET,
            url=url
        )
        if not success or not content:
            raise CaronteTransportError
        exchange_account = ExchangeAccount.from_request(raw_account=content, cpf=message.cpf, status=message.status)
        return exchange_account
