import allure
import pytest
from utility.assertions import assert_response
from utility.emails import get_password_reset_confirm_token_from_email_body




@allure.epic("User Management")
@allure.feature("Authentication password reset")
@pytest.mark.api  
class TestPasswordReset:

    @pytest.fixture(scope="class")
    def new_password(self):
        return "new_strong_password"

    @allure.story("As a activated user, I want to change my password.")
    def test_authenticated_user_password_reser_returns_200(self, auth_api_client, new_password, api_client) :
        assert_response(auth_api_client.authenticated_password_reset(new_password), expected_status=200)
        # Check if password changed successfully
        response = assert_response(auth_api_client.get_profile(), expected_status=200)
        assert_response(api_client.obtain_tokens(response.get("email"), new_password), expected_status=200)

    @allure.story("As a new user, I want to change my password over email, so I have again access to my account")
    def test_not_authenticated_user__password_change_returns_200(self, api_client, new_user_account, new_password):
        user_email = new_user_account.get("email")
        # Send email with reset token if user exist
        assert_response(api_client.api_password_reset(user_email), expected_status=200)
        reset_token = get_password_reset_confirm_token_from_email_body(user_email)
        # Confirm reset token is valid
        assert_response(api_client.api_password_reset_confirm_get(reset_token), expected_status=200)
        # Reset password with reset token
        assert_response(api_client.api_password_reset_confirm(reset_token, new_password), expected_status=200)
        # Check if password changed successfully
        assert_response(api_client.obtain_tokens(user_email, new_password), expected_status=200)



        