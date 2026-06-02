from __future__ import annotations

import time
import uuid
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/v1/gateway", tags=["gateway"])


class GatewayRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    model: str = Field(..., min_length=1)
    metadata: dict[str, Any] | None = None


class GatewayResponse(BaseModel):
    request_id: str
    output_text: str
    provider: str
    latency_ms: int


def _mock_provider_response(prompt: str, model: str) -> tuple[str, str, int]:
    start = time.perf_counter()
    output_text = f"Mock response for model '{model}'"
    provider = "mock"
    latency_ms = int((time.perf_counter() - start) * 1000)
    return output_text, provider, latency_ms


@router.post("/chat", response_model=GatewayResponse)
def gateway_chat(payload: GatewayRequest) -> GatewayResponse:
    request_id = uuid.uuid4().hex
    output_text, provider, latency_ms = _mock_provider_response(
        payload.prompt, payload.model
    )
    return GatewayResponse(
        request_id=request_id,
        output_text=output_text,
        provider=provider,
        latency_ms=latency_ms,
    )
