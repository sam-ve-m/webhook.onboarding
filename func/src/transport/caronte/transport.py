# STANDARD IMPORTS
from decouple import config
import asyncio

# THIRD PART IMPORTS
from caronte import OuroInvestApiTransport


class CaronteTransport:

    @classmethod
    async def get_user_register(cls, cpf: str):
        url = config("OUROINVEST_REGISTER_DATA_URL").format(cpf)
        response = await OuroInvestApiTransport.execute_get_with_default_token(url)
        register_json = await response.json()
        return register_json


if __name__ == '__main__':
    response = asyncio.run(CaronteTransport.get_user_register(
        cpf="71358166099"
    ))
    print(response)
