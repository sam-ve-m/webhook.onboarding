# STANDARD IMPORTS
from decouple import config

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from func.src.domain.exceptions.exceptions import UserWasNotFound
from func.src.infrastructure.mongo_db.infrastructure import MongoDBInfrastructure


class UserRepository:
    infra = MongoDBInfrastructure
    database = config("MONGODB_DATABASE_NAME")
    collection = config("MONGODB_USER_COLLECTION")

    @classmethod
    async def __get_collection(cls):
        mongo_client = cls.infra.get_client()
        try:
            database = mongo_client[cls.database]
            collection = database[cls.collection]
            return collection
        except Exception as ex:
            message = (
                f"UserRepository::__get_collection::Error when trying to get collection"
            )
            Gladsheim.error(
                error=ex,
                message=message,
                database=cls.database,
                collection=cls.collection,
            )
            raise ex

    @classmethod
    async def update_ouroinvest_information(
            cls,
            exchange_account: dict,
            status: str,
            user_filter: dict):

        exchange_account_information = {
            "$set": {
                "ouro_invest.account": exchange_account,
                "ouro_invest.status": status
            }
        }

        collection = await cls.__get_collection()
        was_updated = await collection.update_one(
            user_filter, exchange_account_information
        )

        if not was_updated.matched_count == 1:
            raise UserWasNotFound

        return bool(was_updated)

    @classmethod
    async def update_ouroinvest_user_exchange_account(
            cls,
            cpf: str,
            exchange_account: dict,
            status: str
    ):

        user_filter = {"identifier_document.cpf": cpf}

        try:
            response = await cls.update_ouroinvest_information(
                exchange_account=exchange_account,
                status=status,
                user_filter=user_filter
            )

            return response

            # create log on persephone here

        except UserWasNotFound as ex:
            Gladsheim.error(
                error=ex,
                message="UserRepository::"
                        "update_ouroinvest_exchange_account_information_of_user::"
                        "Failed to update user information",
                query=user_filter,
            )
            return False
