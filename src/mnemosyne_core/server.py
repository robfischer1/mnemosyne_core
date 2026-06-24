"""A standard Forge MCP service.

A standard Forge MCP service: streamable-HTTP, stateless, typed config.
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from mnemosyne_core.settings import get_settings

mcp = FastMCP("mnemosyne-core", stateless_http=True, json_response=True)


@mcp.tool()
def ping() -> dict[str, str]:
    """Liveness sample tool — returns ok. Replace with real tools."""
    return {"status": "ok", "service": "mnemosyne-core"}


def main() -> None:
    """Run the MCP server over streamable-HTTP, binding host:port from settings."""
    settings = get_settings()
    mcp.settings.host = settings.host
    mcp.settings.port = settings.port
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
