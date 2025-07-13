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
    discover_games = await roblox.fetch_discover_games()
    print([
        {
            "sort_id": topic.sort_id,
            "sort_display_name": topic.sort_display_name,
            "applied_filter_detail": topic.applied_filter_detail,
            "games": [
                {
                    "universe_id": game.universe_id,
                    "place_id": game.place_id,
                    "name": game.name,
                    "player_count": game.player_count,
                    "total_up_votes": game.total_up_votes,
                    "total_down_votes": game.total_down_votes,
                    "is_sponsored": game.is_sponsored,
                }
                for game in topic.games
            ],
        }
        for topic in discover_games
    ])


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
