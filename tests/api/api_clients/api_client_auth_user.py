from api.api_clients.api_client_base import ApiClient
import requests
from typing import Dict


class ApiClientAuthUser(ApiClient):
    def __init__(self, base_url, api_tokens = None):
        super().__init__(base_url, api_tokens)

    ##### Private enpoints #########
    def authenticated_password_reset(self, password: str) -> requests.Response:
        payload = {"password": password}
        return self._request("post","/api/user_management/authenticated_password_reset/", json=payload)
    
    def profile_update(self, data: Dict[str, str]) -> requests.Response:
        payload = data
        return self._request("patch","/api/user_management/profile/update/", json=payload)
    
    def get_profile(self) -> requests.Response:
        return self._request("get","/api/user_management/profile/")
    
    def accept_legal_terms(self, data: Dict[str, bool]) -> requests.Response:
        return self._request("post","/api/user_management/legal/accept/", json=data)