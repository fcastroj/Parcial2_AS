from fastapi.testclient import TestClient
from app.adapters.http.fastapi_app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_task():
    res = client.post("/tasks", json={"title": "Tarea 1", "status": "pending"})
    assert res.status_code == 200