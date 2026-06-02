from fastapi.testclient import TestClient

from app.main import app


def test_gateway_chat_valid() -> None:
    client = TestClient(app)
    response = client.post(
        "/v1/gateway/chat",
        json={"prompt": "Hello", "model": "mock-1", "metadata": {"trace_id": "abc"}},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["request_id"]
    assert payload["output_text"]
    assert payload["provider"] == "mock"
    assert isinstance(payload["latency_ms"], int)


def test_gateway_chat_invalid() -> None:
    client = TestClient(app)
    response = client.post("/v1/gateway/chat", json={})

    assert response.status_code == 422
