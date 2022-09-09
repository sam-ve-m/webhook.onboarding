from decouple import config
from etria_logger import Gladsheim

from src.domain.models.exchange_account.model import ExchangeAccount
from src.infrastructure.mongo_db.infrastructure import MongoDBInfrastructure


class UserRepository:
    infra = MongoDBInfrastructure

    @classmethod
    async def __get_collection(cls):
        mongo_client = cls.infra.get_client()
        try:
            database = mongo_client[config("MONGODB_DATABASE_NAME")]
            collection = database[config("MONGODB_USER_COLLECTION")]
            return collection
        except Exception as ex:
            message = (
                f"UserRepository::__get_collection::Error when trying to get collection"
            )
            Gladsheim.error(
                error=ex,
                message=message,
                database=config("MONGODB_DATABASE_NAME"),
                collection=config("MONGODB_USER_COLLECTION"),
            )
            raise ex

    @classmethod
    async def find_client_unique_id(cls, cpf: str) -> str:
        user_filter = {"identifier_document.cpf": cpf}
        collection = await cls.__get_collection()
        user = await collection.find_one(user_filter) or {}
        unique_id = user.get("unique_id")
        return unique_id

    @classmethod
    async def update_exchange_account(cls, exchange_account: ExchangeAccount) -> bool:
        user_filter = {"identifier_document.cpf": exchange_account.cpf}
        exchange_account_information = {
            "$set": {
                "ouro_invest.account": exchange_account.account,
                "ouro_invest.status": exchange_account.status
            }
        }

        collection = await cls.__get_collection()
        was_updated = await collection.update_one(
            user_filter, exchange_account_information
        )
        return was_updated.matched_count == 1
