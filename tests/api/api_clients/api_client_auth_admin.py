from api.api_clients.api_client_base import ApiClient
import requests


class ApiClientAuthAdmin(ApiClient):
    def __init__(self, base_url, api_tokens = None):
        super().__init__(base_url, api_tokens)

    ######  Admin endpoints ######
    def api_delete_user(self, username: str) -> requests.Response:
        return self._request("delete", f"/api/user_management/admin/delete_abo_user/",   params={"username": username})