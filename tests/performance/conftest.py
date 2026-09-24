import pytest
import csv
from pathlib import Path


@pytest.fixture
def jmeter_user_account(request, api_client, clean_mailpit):
    """Create the account consumed by the JMeter CSV data set."""
    from utility.emails import get_activation_token_from_email_body
    from utility.factories import make_user_data_abonament_basic

    user_data = make_user_data_abonament_basic()
    response = api_client.api_register_user(**user_data)
    assert response.status_code == 201, f"Failed to create user: {response.text}"

    activation_token = get_activation_token_from_email_body(user_data["email"])
    response = api_client.api_activate_user(activation_token)
    assert response.status_code == 302, f"Failed to activate user: {response.text}"

    csv_path = Path(__file__).parent / "data" / "jmeter_test_users.csv"
    file_mode = "w" if request.param == 1 else "a"
    with csv_path.open(file_mode, newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=("username", "password"))
        if file_mode == "w":
            writer.writeheader()
        writer.writerow({"username": user_data["email"], "password": user_data["password"]})

    return user_data