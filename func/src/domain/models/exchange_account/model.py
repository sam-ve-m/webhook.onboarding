from dataclasses import dataclass


@dataclass
class ExchangeAccount:
    cpf: str
    status: str
    account: dict

    def log_schema(self, unique_id: str) -> dict:
        message = {
            "unique_id": unique_id,
            "status": self.status,
            "cpf": self.cpf,
            "exchange_account": self.account,
        }
        return message

    @classmethod
    def from_request(cls, raw_account: dict, **kwargs):
        bank_account = raw_account.get("dadosBancarios", {})
        exchange_account = {
            "client_id": raw_account.get("cliente", {}).get("codigoCliente"),
            "codigo_ISPB": bank_account.get("codigoISPB"),
            "numero_agencia": bank_account.get("numeroAgencia"),
            "digito_agencia": bank_account.get("digitoAgencia"),
            "numero_conta": bank_account.get("numeroConta"),
            "digito_conta": bank_account.get("digitoConta"),
            "numero_banco": bank_account.get("numeroBanco"),
            "nome_banco": bank_account.get("nomeBanco"),
            "conta_principal": bank_account.get("contaPrincipal"),
        }
        return cls(account=exchange_account, **kwargs)
