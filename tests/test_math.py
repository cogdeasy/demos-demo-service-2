import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "features" in data


def test_add():
    response = client.post("/api/math/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8


def test_add_negative():
    response = client.post("/api/math/add?a=-5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == -2
