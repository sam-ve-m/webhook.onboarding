# STANDARD IMPORTS
# import os
# from unittest import mock
# from unittest.mock import patch, MagicMock
#
# import pytest
# # PROJECT IMPORTS
# from persephone_client import Persephone
# from src.services.persephone.service import SendToPersephone
#
# exchange_account_stub = {"exchange_dict": "1234567"}
# cpf_stub = "43426789810"
# status_stub = "Em Análise"
# unique_id = "635jdhfbmvkhdidif8374654"
#
# stub_response = {
#     'cpf': '43426789810',
#     'exchange_account': {'exchange_dict': '1234567'},
#     'status': 'Em Análise',
#     'unique_id': '635jdhfbmvkhdidif8374654'
# }
#
#
# @pytest.mark.asyncio
# @patch.object(Persephone, "send_to_persephone", return_value=MagicMock())
# async def test_when_sending_right_params_to_register_user_exchange_member_log_then_return_expected(
#         mock_send_to_persephone
# ):
#     response = await SendToPersephone.register_user_exchange_member_log(
#         unique_id=unique_id,
#         status=status_stub,
#         cpf=cpf_stub,
#         exchange_account=exchange_account_stub
#     )
#     assert response == ""
