from fastmcp import FastMCP
from rbxclient.client import RBXClient
from keyring import get_password

roblox = RBXClient(get_password("ROBLOX_MCP_SERVER", ".ROBLOXSECURITY"))


async def main():
    friends = await roblox.fetch_friends(with_presence=True)
    print(friends)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
