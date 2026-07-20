from __future__ import annotations

import time

from app.adapters.base import ProviderAdapter, ProviderError, ProviderResponse


class MockProviderAdapter(ProviderAdapter):
    def call(self, prompt: str, model: str) -> ProviderResponse:
        start = time.perf_counter()
        if model == "mock-error":
            raise ProviderError("Mock provider failure")

        output_text = f"Mock response for model '{model}'"
        latency_ms = int((time.perf_counter() - start) * 1000)
        return ProviderResponse(output_text=output_text, latency_ms=latency_ms)
