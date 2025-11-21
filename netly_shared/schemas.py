import datetime

from enum import Enum
from pydantic import BaseModel, field_validator
from typing import List, Optional, Dict, Any


class Status(str, Enum):
    SUCCESS = "Success"
    FAILED = "Failed"


# Each service result
class ServiceResult(BaseModel):
    service_name: str
    status: Status
    parameters_used: Optional[Dict[str, Any]]
    output: Optional[str]
    execution_time_ns: Optional[int]
    metadata: Optional[Dict[str, Any]]


class Service(BaseModel):
    service_name: str
    parameters: Optional[Dict[str, Any]] = None

    @field_validator("service_name")
    @classmethod
    def no_spaces(cls, v: str) -> str:
        if " " in v:
            raise ValueError("service_name cannot contain spaces")
        return v


class ServerRequest(BaseModel):
    API_KEY: str
    HOST_ID: str
    request_id: str
    timestamp: str
    services: List[Service]

    @field_validator("timestamp")
    @classmethod
    def check_timestamp(cls, v: str) -> str:
        try:
            datetime.datetime.fromisoformat(v)
        except ValueError as e:
            raise
        return v


# Top-level feedback model
class ClientFeedback(BaseModel):
    host_id: str
    api_key: str
    execution_id: str
    timestamp: str
    overall_status: str
    total_services: int
    successful_services: int
    failed_services: int
    results: List[ServiceResult]

    @field_validator("timestamp")
    @classmethod
    def check_timestamp(cls, v: str) -> str:
        try:
            datetime.datetime.fromisoformat(v)
        except ValueError as e:
            raise
        return v


example_data = {
    "host_id": "foo",
    "api_key": "bar",
    "execution_id": "exec_20231201_123456",
    "timestamp": "2023-12-01T12:34:56.123456Z",
    "overall_status": "success",
    "total_services": 1,
    "successful_services": 1,
    "failed_services": 0,
    "results": [
        {
            "service_name": "docker",
            "status": "success",
            "parameters_used": {"container_name": "my_container"},
            "output": "Container started successfully",
            "execution_time_ns": 2500,
            "metadata": {
                "container_name": "my_container",
                "container_image": "my_container_image:latest",
                "exposed_ports": 5051,
            },
        }
    ],
}

# _mydata = ClientFeedback(**example_data)
