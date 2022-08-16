# STANDARD IMPORTS
from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 0
    JWT_INVALID = 30
    INTERNAL_SERVER_ERROR = 100
    INVALID_ONBOARDING_STEP = 49
    TRANSPORT_LAYER_ERROR = 69
    USER_WAS_NOT_FOUND = 99

    def __repr__(self):
        return self.value
