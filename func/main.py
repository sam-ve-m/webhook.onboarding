# STANDARD IMPORTS
from http import HTTPStatus
from aioflask import Flask
from flask import request, Response, Request

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from func.src.domain.enums.status_code.enum import InternalCode
from func.src.domain.models.response.model import ResponseModel


app = Flask(__name__)


@app.route('/put/update_exchange_account')
async def update_exchange_account_information(request: Request = request) -> Response:

    try:
        # exchange_member = ExchangeMemberRequest(**request_body.json)
        #
        # service_response = await UpdateExchangeMember.update_exchange_member_us(
        #     jwt_data=jwt_data,
        #     exchange_member_request=exchange_member
        # )

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
