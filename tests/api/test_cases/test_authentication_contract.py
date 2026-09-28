import pytest 
import schemathesis
import allure

# Define and filter the schema at module level for test collection
schema_user_management_token = (
    schemathesis.pytest.from_fixture("api_schema")
    .include(path="/api/user_management/token/", method="POST")
)

schema_user_management_token_refresh = (
    schemathesis.pytest.from_fixture("api_schema")
    .include(path="/api/user_management/token/refresh/", method="POST")
)


@pytest.mark.contract
@allure.epic("API Authentication & Onboarding")
@allure.feature("User management")
@allure.story("Schema contract is checked")
class TestUserManagementContract:


    @schema_user_management_token.parametrize()
    def test_user_management_contract_token(self, case, api_base_url):
        case.call_and_validate(base_url=api_base_url)

    @schema_user_management_token_refresh.parametrize()
    def test_user_management_contract_token_refresh(self, case, api_base_url):
        case.call_and_validate(base_url=api_base_url)

    # Chain filters to narrow down the test scope
    # filtered_schema = (
    #     schema
    #     #.exclude(path_regex="^/api/user_management/password_reset")
    #     .include(path="/api/user_management/token/", method="POST")
    #     #.include(path="/api/user_management/token/refresh/", method="POST")
    #     #.include(path="/api/user_management/legal/accept/", method="POST")
    #     #.include(path="/api/user_management/profile/", method="GET")
    #     #.include(path="/api/aktualnosci/threads/", method="POST")
        

    #     #.include(path="/api/user_management/password_reset/", method="POST") # Sends password reset instructions to the provided email if it exists in the system
    #     #.include(path="/api/user_management/password_reset_confirm/{token}/", method="GET") # Checks if password reset token exists and can be used.
    #     #.include(path="/api/user_management/password_reset_confirm/{token}/", method="POST") # Resets user password using valid reset token and clears the token.
    #     #.include(path_regex="^/api/v1/")      # Only test the v1 API
    #     #.exclude(path="/api/v1/internal")     # Exclude an exact path
    #     #.exclude(method="DELETE")             # Skip all DELETE operations
    #     #.exclude(tag="experimental")          # Skip endpoints tagged as 'experimental'
    #     #.exclude(operation_id="resetDB")      # Exclude a specific operation ID
    # )





