# Roblox MCP Server

A custom MCP (Multi-Channel Presence) server built to enhance the Roblox experience by enabling real-time friend presence tracking and seamless game joining.

## Features

- 🔍 Fetch real-time presence information of your Roblox friends.
- 🎮 Display a list of friends who are currently in-game.
- 🚀 Join a friend’s game directly via Roblox deep links.

![DemoVideo](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b9b16af8eeca3d65ff7193048549ea330abfe448_screen_recording_2025-07-13_at_11.26.11___pm.mp4)

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/roblox-mcp-server.git
   
2. Navigate to the project directory:
   ```bash
    cd roblox-mcp-server
    ```
3. Install the required dependencies:
```bash
uv sync
```

4. Add mcp server to Claude config:
```json
{
    "mcpServers": {
        "roblox": {
            "command": "python3",
            "args": [
                "-m",
                "uv",
                "--directory",
                "/[Change this to your directory]/roblox-mcp-server",
                "run",
                "main.py"
            ]
        }
    }
}
```

5.Try roblox mcp server on Claude Desktop