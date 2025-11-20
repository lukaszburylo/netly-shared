from typing import Optional
import json


class ResponseTemplate:
    response: dict

    @classmethod
    def __init__(
        cls,
        service_name: str,
        result_status: bool,
        input_data: Optional[str] = None,
        output_data: Optional[str] = None,
    ):
        cls.response = {
            "service_name": service_name,
            "result_status": "Success" if result_status else "Error",
            "input_data": input_data,
            "output_data": output_data,
        }

    @classmethod
    def __str__(cls) -> str:
        return json.dumps(cls.response)

    @classmethod
    def get_response(cls):
        return cls.response
