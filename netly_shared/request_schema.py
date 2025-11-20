from pydantic import BaseModel, field_validator, ValidationError
from typing import List, Optional, Dict, Any
from datetime import datetime


class Service(BaseModel):
    service_name: str
    parameters: Optional[Dict[str, Any]] = None

    @field_validator('service_name')
    @classmethod
    def no_spaces(cls, v: str) -> str:
        if ' ' in v:
            raise ValueError('service_name cannot contain spaces')
        return v

class Request(BaseModel):
    API_KEY: str
    HOST_ID: str
    request_id: str
    timestamp: datetime
    services: List[Service]

example_data = {
    "API_KEY": "foo",
    "HOST_ID": "bar",
    "request_id": "20231201_123456",
    "timestamp": "2023-12-01T12:34:56.123456Z",
    "services": [
        {
            "service_name": "docker",
            "parameters": {"container_name": "my_container"},
        },
        {
            "service_name": "ip_address"
        },
        {
            "service_name": "fake",
            "parameters": {}
        }
    ]
}

_mydata = Request(**example_data)
