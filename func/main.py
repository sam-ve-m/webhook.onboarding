# STANDARD IMPORTS
from http import HTTPStatus
from aioflask import Flask
from flask import request, Response, Request

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from func.src.domain.enums.status_code.enum import InternalCode
from func.src.domain.models.response.model import ResponseModel
from func.src.domain.models.web_hook.model import ClientDataRequest


app = Flask(__name__)


@app.route('/put/save_exchange_account')
async def update_exchange_account_information(request_body: Request = request) -> Response:
    message, cpf = ClientDataRequest.get_message_and_cpf(request_body)

    try:
        

        service_response = 0

        response = ResponseModel(
            success=True,
            code=InternalCode.SUCCESS,
            message="Data Was Successfully Updated",
            result=service_response
        ).build_http_response(status=HTTPStatus.OK)
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
