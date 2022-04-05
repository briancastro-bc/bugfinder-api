from typing import Union
from pydantic import BaseSettings, AnyHttpUrl, validator

__all__: list[str] = ["settings"]

"""
    :class _Settings - Set up all configurations from the .env file
    for the application.
"""
class _Settings(BaseSettings):
    # CORS
    CORS_ORIGINS: list[AnyHttpUrl]
    
    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, value: Union[str, list[str]]) -> Union[list[str], str]:
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]
        elif isinstance(value, (list, str)):
            return value
        raise ValueError(value)
    
    class Config:
        env_file='.env'
        case_sensitive=True

settings = _Settings()