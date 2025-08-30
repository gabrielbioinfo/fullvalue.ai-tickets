"""Configuration loader module for application settings.

This module defines the ConfigLoader class for managing environment-based configuration using Pydantic.
"""

from typing import ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class ConfigLoader(BaseSettings):
    """Configuration settings for the application."""

    env_file: ClassVar[str] = ".env"
    env_file_encoding: ClassVar[str] = "utf-8"

    project_name: str = "bars-backend"

    app_host: str = "0.0.0.0"  # noqa: S104
    app_port: int = 8000

    open_api_key: str = ""
    open_api_model: str = ""

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0


config = ConfigLoader()
