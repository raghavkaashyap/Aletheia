from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel


class ProviderResponse(BaseModel):
    output_text: str
    latency_ms: int


class ProviderAdapter(ABC):
    @abstractmethod
    def call(self, prompt: str, model: str) -> ProviderResponse:
        raise NotImplementedError
