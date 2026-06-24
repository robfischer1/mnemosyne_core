"""Typed runtime configuration for mnemosyne-core.

Settings resolve from (lowest to highest precedence): the code defaults below
-> environment variables prefixed `MNEMOSYNE_CORE_`. Validation runs
at construction, so a malformed value fails fast at startup instead of deep in a
request path. Add fields below; type any secret as `pydantic.SecretStr` so it
never surfaces in logs or repr.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Process configuration, validated from the environment."""

    model_config = SettingsConfigDict(
        env_prefix="MNEMOSYNE_CORE_",
        extra="ignore",
    )

    log_level: str = "INFO"
    host: str = "0.0.0.0"  # noqa: S104 — operator-chosen HTTP bind host
    port: int = 8201


@lru_cache
def get_settings() -> Settings:
    """Return the process-wide settings singleton (constructed once)."""
    return Settings()
