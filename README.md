# Netly Shared Schemas

This module defines Pydantic models used across Netly for service requests, service definitions, results and client feedback.

See the implementation: [netly_shared/schemas.py](netly_shared/schemas.py)

## Models

- [`netly_shared.schemas.Status`](netly_shared/schemas.py) — Enum for service result status (`"Success"` | `"Failed"`).
- [`netly_shared.schemas.ServiceResult`](netly_shared/schemas.py) — Per-service result payload.
- [`netly_shared.schemas.Service`](netly_shared/schemas.py) — Service descriptor (validates `service_name` has no spaces).
- [`netly_shared.schemas.ServerRequest`](netly_shared/schemas.py) — Incoming request model (validates ISO timestamp).
- [`netly_shared.schemas.ClientFeedback`](netly_shared/schemas.py) — Aggregated feedback model (validates ISO timestamp).
- [`netly_shared.schemas.example_data`](netly_shared/schemas.py) — Example payload demonstrating the expected shape.

## Validation notes

- `Service.service_name` must not contain spaces.
- `ServerRequest.timestamp` and `ClientFeedback.timestamp` are validated with `datetime.fromisoformat` — provide a valid ISO-8601 string.

## Quick usage

```python
# Example usage
from netly_shared.schemas import (
    Service,
    ServiceResult,
    ServerRequest,
    ClientFeedback,
    example_data,
)

# Create a model from dict
cf = ClientFeedback(**example_data)
print(cf.total_services)
```

## Development

- The module uses Pydantic for validation. Install requirements from `requirements.txt` and `requirements-dev.txt` for tests and linting.
- File: [netly_shared/schemas.py](netly_shared/schemas.py)