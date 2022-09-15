import pytest
from app import app as flask_app


@pytest.fixture
def appl():
    yield flask_app


@pytest.fixture
def client(appl):
    return appl.test_client()


# Smoke test Flask
def test_index(appl, client):
    res = client.get("/")
    assert res.status_code == 200
    assert "Diabetes prediction API." in res.get_data(as_text=True)
