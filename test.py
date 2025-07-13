from fastmcp import FastMCP
from rbxclient.client import RBXClient

key = open("key.txt", "r").read().strip()
print(key)

roblox = RBXClient(key)


async def main():
    friends = await roblox.fetch_friends(with_presence=True)
    print(friends)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
