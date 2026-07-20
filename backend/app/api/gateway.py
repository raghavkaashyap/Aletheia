from __future__ import annotations

import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.adapters import MockProviderAdapter, ProviderError
from app.adapters import MockProviderAdapter
from app.db import get_session
from app.models import GatewayRequest as GatewayRequestRecord

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


class GatewayErrorDetail(BaseModel):
    error: str
    message: str


@router.post("/chat", response_model=GatewayResponse)
def gateway_chat(
    payload: GatewayRequest,
    session: Session = Depends(get_session),
) -> GatewayResponse:
    request_id = uuid.uuid4().hex
    try:
        provider_response = _adapter.call(payload.prompt, payload.model)
    except ProviderError as exc:
        error_detail = GatewayErrorDetail(
            error="provider_error",
            message=exc.public_message,
        )
        raise HTTPException(status_code=502, detail=error_detail.model_dump()) from exc

    return GatewayResponse(
    provider_response = _adapter.call(payload.prompt, payload.model)
    response = GatewayResponse(
        request_id=request_id,
        output_text=provider_response.output_text,
        provider="mock",
        latency_ms=provider_response.latency_ms,
    )
    session.add(
        GatewayRequestRecord(
            request_id=response.request_id,
            prompt=payload.prompt,
            model=payload.model,
            provider=response.provider,
            response_text=response.output_text,
            latency_ms=response.latency_ms,
        )
    )
    session.commit()
    return response
