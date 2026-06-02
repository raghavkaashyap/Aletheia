from __future__ import annotations

import uuid
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.adapters import MockProviderAdapter

router = APIRouter(prefix="/v1/gateway", tags=["gateway"])
_adapter = MockProviderAdapter()


class GatewayRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    model: str = Field(..., min_length=1)
    metadata: dict[str, Any] | None = None


class GatewayResponse(BaseModel):
    request_id: str
    output_text: str
    provider: str
    latency_ms: int


@router.post("/chat", response_model=GatewayResponse)
def gateway_chat(payload: GatewayRequest) -> GatewayResponse:
    request_id = uuid.uuid4().hex
    provider_response = _adapter.call(payload.prompt, payload.model)
    return GatewayResponse(
        request_id=request_id,
        output_text=provider_response.output_text,
        provider="mock",
        latency_ms=provider_response.latency_ms,
    )
