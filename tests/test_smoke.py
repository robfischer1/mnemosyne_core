"""Smoke tests for mnemosyne-core."""

import re

from mnemosyne_core import __version__
from mnemosyne_core.server import mcp, ping
from mnemosyne_core.settings import get_settings


def test_version() -> None:
    # Assert a valid X.Y.Z version rather than a frozen literal, so the test
    # survives version bumps instead of rotting into a CI break.
    assert re.fullmatch(r"\d+\.\d+\.\d+", __version__)


def test_settings_load() -> None:
    assert get_settings().log_level == "INFO"


def test_ping_tool() -> None:
    assert ping()["status"] == "ok"


def test_server_name() -> None:
    assert mcp.name == "mnemosyne-core"
