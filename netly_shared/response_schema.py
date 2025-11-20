from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

# Metadata for each service result
class ServiceMetadata(BaseModel):
    container_name: Optional[str]
    container_image: Optional[str]
    exposed_ports: Optional[int]

# Each service result
class ServiceResult(BaseModel):
    service_name: str
    status: str
    parameters_used: Optional[Dict[str, Any]]
    output: Optional[str]
    execution_time_ms: Optional[int]
    metadata: Optional[ServiceMetadata]

# Top-level feedback model
class ClientFeedback(BaseModel):
    host_id: str
    api_key: str
    execution_id: str
    timestamp: datetime
    overall_status: str
    total_services: int
    successful_services: int
    failed_services: int
    results: List[ServiceResult]


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
            "execution_time_ms": 2500,
            "metadata":
                {
                    "container_name": "my_container",
                    "container_image": "my_container_image:latest",
                    "exposed_ports": 5051
                }
        }
    ]
}

_mydata = ClientFeedback(**example_data)