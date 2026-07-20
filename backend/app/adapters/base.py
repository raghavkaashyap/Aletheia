from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel


class ProviderResponse(BaseModel):
    output_text: str
    latency_ms: int


class ProviderError(Exception):
    def __init__(
        self,
        message: str = "Provider request failed",
        public_message: str = "Provider request failed",
    ) -> None:
        self.message = message
        self.public_message = public_message
        super().__init__(message)


class ProviderAdapter(ABC):
    @abstractmethod
    def call(self, prompt: str, model: str) -> ProviderResponse:
        raise NotImplementedError
