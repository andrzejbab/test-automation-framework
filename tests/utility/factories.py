import uuid

def make_user_data_abonament_basic() -> dict:
    """Generate dynamic payload for user creation."""
    unique_id = uuid.uuid4().hex[:8]
    data = {
        "email": f"testuser_{unique_id}@test.local",
        "password": "test_password123!",
        "accept_terms": True,
        "accept_privacy_policy": True,
        "abonament": "basic"
    }
    return data