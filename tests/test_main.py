from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["message"]
    assert payload["app"] == "fde-agent"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "healthy"


def test_agent_research_endpoint():
    response = client.post(
        "/api/agent/research",
        json={
            "query": "How can AI reduce operational bottlenecks?",
            "context": "customer support workflow",
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["query"] == "How can AI reduce operational bottlenecks?"
    assert payload["summary"]
    assert isinstance(payload["recommended_actions"], list)
    assert len(payload["recommended_actions"]) >= 1
