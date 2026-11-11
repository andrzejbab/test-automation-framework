import pytest

@pytest.mark.prepare_pydantic_models
def test_create_pydantic_models(generate_pydantic_models):
    assert True