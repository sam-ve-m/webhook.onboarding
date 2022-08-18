# STANDARD IMPORTS
from http import HTTPStatus
from aioflask import Flask
from flask import request, Response, Request

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from func.src.domain.enums.status_code.enum import InternalCode
from func.src.domain.exceptions.exceptions import UserWasNotFound, CaronteTransportError, StatusSentIsNotValid
from func.src.domain.models.response.model import ResponseModel
from func.src.domain.models.web_hook.model import ClientDataRequest
from func.src.services.web_hook.service import UpdateOuroInvestInformation


app = Flask(__name__)


@app.route('/put/save_exchange_account')
async def update_exchange_account_information(request_body: Request = request) -> Response:
    hook_request = request_body.json

    try:
        client_data = ClientDataRequest(request_body=hook_request)

        service_response = await UpdateOuroInvestInformation.update_ouroinvest_exchange_account(
            client_data=client_data
        )

        response = ResponseModel(
            success=True,
            code=InternalCode.SUCCESS,
            message="Data Was Successfully Updated",
            result=service_response
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except UserWasNotFound as error:
        Gladsheim.error(error=error)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.USER_WAS_NOT_FOUND,
            message="USER WAS NOT FOUND"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except CaronteTransportError as error:
        Gladsheim.error(error=error)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.CARONTE_TRANSPORT_ERROR,
            message="ERROR ON FETCHING DATA FROM CARONTE TRANSPORT"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except StatusSentIsNotValid as error:
        Gladsheim.error(error=error)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.STATUS_SENT_IS_NOT_A_VALID_ENUM,
            message="ERROR ON FETCHING DATA FROM CARONTE TRANSPORT"
        ).build_http_response(status=HTTPStatus.BAD_REQUEST)
        return response

    except Exception as error:
        Gladsheim.error(error=error)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.INTERNAL_SERVER_ERROR,
            message="Unexpected error occurred"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

if __name__ == "__main__":
    app.run(debug=True)
