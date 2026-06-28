from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.db import Base, get_session
from app.main import app
from app.models import GatewayRequest as GatewayRequestRecord


@pytest.fixture()
def test_sessionmaker() -> sessionmaker[Session]:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    return sessionmaker(autoflush=False, autocommit=False, bind=engine)


@pytest.fixture()
def client(test_sessionmaker: sessionmaker[Session]) -> Generator[TestClient, None, None]:
    def override_get_session() -> Generator[Session, None, None]:
        with test_sessionmaker() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_gateway_chat_valid(client: TestClient) -> None:
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


def test_gateway_chat_persists_request(
    client: TestClient,
    test_sessionmaker: sessionmaker[Session],
) -> None:
    response = client.post(
        "/v1/gateway/chat",
        json={"prompt": "Persist me", "model": "mock-1"},
    )

    assert response.status_code == 200
    payload = response.json()

    with test_sessionmaker() as session:
        record = session.scalar(
            select(GatewayRequestRecord).where(
                GatewayRequestRecord.request_id == payload["request_id"]
            )
        )

    assert record is not None
    assert record.prompt == "Persist me"
    assert record.model == "mock-1"
    assert record.provider == "mock"
    assert record.response_text == payload["output_text"]
    assert record.latency_ms == payload["latency_ms"]


def test_gateway_chat_invalid(client: TestClient) -> None:
    response = client.post("/v1/gateway/chat", json={})

    assert response.status_code == 422
