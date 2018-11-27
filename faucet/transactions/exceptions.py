from rest_framework.exceptions import APIException


class TransactionError(Exception):
    """Exception in combination with a transaction.
    """

    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


class RpcConnectionError(TransactionError):
    """Exception in combination with wallet RPCs.
    """


class GetWalletError(TransactionError):
    """Exception in combination with
    getting/calculating the tarnsaction's amount.
    """


class GetBalanceError(APIException):
    status_code = 500
    default_detail = "RPC Error on getting balance."


class GetAmountError(APIException):
    status_code = 500
    default_detail = "RPC Error on getting amount."


class MakeTransactionError(APIException):
    status_code = 500
    default_detail = "Could not make transaction."
