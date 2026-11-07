from pydantic import BaseModel


class ApiUserManagementActivate(BaseModel):
    error: str

class TokenRefreshUnauthorized(BaseModel):
    detail: str
    code: str