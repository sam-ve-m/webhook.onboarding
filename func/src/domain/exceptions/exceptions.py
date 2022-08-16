class ErrorOnDecodeJwt(Exception):
    msg = "Jormungandr-Onboarding::decode_jwt_and_get_unique_id::Fail when trying to get unique_id," \
          " jwt not decoded successfully"


class TransportOnboardingError(Exception):
    msg = "Jormungandr-Onboarding::ValidateOnboardingSteps::error on fetching data from fission steps"


class UserWasNotFound(Exception):
    msg = "Jormungandr-Onboarding::UserRepository::update_user_and_broker_member - user was not found"
