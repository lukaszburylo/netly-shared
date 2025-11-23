"""Configuration schema definitions for Netly client and server."""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class ServiceConfig(BaseModel):
    """Service configuration model"""

    service_name: str
    parameters: Dict[str, Any]


class HostConfig(BaseModel):
    """Host configuration model"""

    host_id: str
    api_key: str
    services: List[ServiceConfig]


class ClientConfig(BaseModel):
    """Client configuration model"""

    host: str
    api_key: str
    server_ip: str
    server_port: int


class ServerConfig(BaseModel):
    """Server configuration model"""

    ip: str
    port: int
    hosts: List[HostConfig]


class AppConfig(BaseModel):
    """Top-level application configuration model"""

    client: Optional[ClientConfig] = None
    server: Optional[ServerConfig] = None
