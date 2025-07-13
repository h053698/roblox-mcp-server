from fastmcp import FastMCP
from rbxclient.client import RBXClient

key = open("key.txt", "r").read().strip()
print(key)

mcp = FastMCP("Roblox MCP")
roblox = RBXClient(key)


@mcp.tool
async def get_authenticated_user() -> dict:
    "get the authenticated user information"
    user_me = await roblox.client.get_authenticated_user()
    return {
        "id": user_me.id,
        "name": user_me.name,
        "display_name": user_me.display_name,
        "description": user_me.description,
        "is_banned": user_me.is_banned,
        "created": user_me.created.isoformat(),
    }


@mcp.tool
async def get_robux_balance() -> int:
    robux_balance = await roblox.fetch_robux_balance()
    return robux_balance


@mcp.tool
async def open_game_with_friends(
    game_id: int,
    user_id: int = None,
) -> dict:
    "open a game with friends using the Roblox deeplink"
    roblox.deeplink.open_game(game_id, user_id)
    return {"success": True}


@mcp.tool
async def get_friends() -> list[dict]:
    "get the authenticated user's friends"
    friends = await roblox.fetch_friends(with_presence=True)
    return [
        {
            "id": friend.id,
            "name": friend.name,
            "display_name": friend.display_name,
            "presence": [
                (
                    {
                        "status": (
                            friend.presence.status.value if friend.presence else None
                        ),
                        "name": friend.presence.name if friend.presence else None,
                        "game": [
                            (
                                {
                                    "id": [
                                        (
                                            friend.presence.game.id
                                            if friend.presence and friend.presence.game
                                            else None
                                        )
                                    ],
                                    "place_id": [
                                        (
                                            friend.presence.game.place_id
                                            if friend.presence and friend.presence.game
                                            else None
                                        )
                                    ],
                                    "root_place_id": [
                                        (
                                            friend.presence.game.root_place_id
                                            if friend.presence and friend.presence.game
                                            else None
                                        )
                                    ],
                                }
                                if friend.presence
                                else None
                            )
                        ],
                    }
                    if friend.presence
                    else None
                )
            ],
        }
        for friend in friends
    ]


if __name__ == "__main__":
    mcp.run()
