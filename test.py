import keyring
from fastmcp import FastMCP

from credential_manager import open_app
from rbxclient.client import RBXClient
from keyring import get_password

SERVICE_ID = "ROBLOX_MCP_SERVER"
USERNAME = ".ROBLOXSECURITY"

key = keyring.get_password(SERVICE_ID, USERNAME)
roblox = RBXClient(key)


async def main():
    open_app()
    await roblox.set_roblox_auth_key(
        get_password("ROBLOX_MCP_SERVER", ".ROBLOXSECURITY")
    )
    friends = await roblox.fetch_discover_games()
    print(friends)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
