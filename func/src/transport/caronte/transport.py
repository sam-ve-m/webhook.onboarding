# STANDARD IMPORTS
import asyncio
from decouple import config

# THIRD PART IMPORTS
from caronte import OuroInvestApiTransport
from etria_logger import Gladsheim

# PROJECT IMPORTS
from func.src.domain.exceptions.exceptions import CaronteTransportError


class CaronteTransport:

    @classmethod
    async def get_user_register(cls, cpf: str):
        url = config("OUROINVEST_REGISTER_DATA_URL").format(cpf)

        try:
            response = await OuroInvestApiTransport.execute_get_with_default_token(
                url=url
            )
            register_json = await response.json()
            return register_json

        except Exception as error:
            Gladsheim.error(error=error)
            raise CaronteTransportError
