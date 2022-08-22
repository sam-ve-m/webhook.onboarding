class LogOuroInvestToPersephone:

    @classmethod
    def ouroinvest_schema_message(
            cls,
            exchange_account: dict,
            cpf: str,
            status: str,
            unique_id: str
    ) -> dict:
        message = {
            "unique_id": unique_id,
            "status": status,
            "cpf": cpf,
            "exchange_account": exchange_account
        }

        return message
