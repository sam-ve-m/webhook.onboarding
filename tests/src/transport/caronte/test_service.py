# STANDARD IMPORTS
# from unittest.mock import patch
# import pytest

# PROJECT IMPORTS
# from caronte import OuroInvestApiTransport
# from api_response import api_response_stub
# from func.src.transport.caronte.transport import CaronteTransport


# @pytest.mark.asyncio
# @patch.object(OuroInvestApiTransport, "execute_get_with_default_token", return_value=api_response_stub)
# async def test_when_sending_right_params_to_get_user_register_then_return_the_expected(
#         mock_execute_get_with_default_token
# ):
#     response = await CaronteTransport.get_user_register(
#         cpf="45469898650"
#     )
#     assert response == ""
