import pytest

# Technical testcases only for intern use of taurus jmeter to reuse fixture 
@pytest.mark.jmeter_prepare
def test_create_users(jmeter_new_user_accounts):
    assert True




