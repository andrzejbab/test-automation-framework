# from http import HTTPStatus

# import pytest
# import httpx

# from tests.openapi.openapi_client.klubster_api_client import Client  
# from tests.openapi.openapi_client.klubster_api_client.api.authentication import user_management_token_create as token_create_api
# from tests.openapi.openapi_client.klubster_api_client.models.user_management_token_create_body import UserManagementTokenCreateBody
# from tests.openapi.openapi_client.klubster_api_client.models.user_management_token_create_response_200 import UserManagementTokenCreateResponse200



# @pytest.mark.api
# @pytest.mark.skip("Only for test Open api client and httpx")
# def test_token_obtain_pair_openapi_client(api_base_url, new_user_account):

#     username = new_user_account.get("email")
#     password = new_user_account.get("password")

#     if not api_base_url or not username or not password:
#         pytest.skip("API base URL or credentials are missing")

#     payload = UserManagementTokenCreateBody(username=username, password=password)
#     try:
#         client = Client(base_url=api_base_url)
#         response = token_create_api.sync_detailed(client=client, body=payload)
#     except httpx.RequestError as exc:
#         pytest.skip(f"API not reachable: {exc}")
#     finally:
#         client.get_httpx_client().close()
        
#     assert response.status_code == HTTPStatus.OK
#     assert isinstance(response.parsed, UserManagementTokenCreateResponse200)
#     assert response.parsed.access
#     assert response.parsed.refresh
