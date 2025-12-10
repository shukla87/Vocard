import os, json

settings = {
    "token": os.getenv("TOKEN"),
    "client_id": os.getenv("CLIENT_ID"),
    "genius_token": os.getenv("GENIUS_TOKEN"),
    "mongodb_url": os.getenv("MONGODB_URL"),
    "mongodb_name": os.getenv("MONGODB_NAME"),
    "nodes": {
        "DEFAULT": {
            "host": "lavalink",
            "port": 2333,
            "password": "youshallnotpass",
            "secure": False,
            "identifier": "DEFAULT",
            "yt_ratelimit": {
                "tokens": [],
                "config": {
                    "retry_time": 10800,
                    "max_requests": 30
                },
                "strategy": "LoadBalance"
            }
        }
    },
    "prefix": "?",
    "activity": [
        {"type": "listening", "name": "/help", "status": "online"}
    ],
    "logging": {
        "file": {
            "path": "./logs",
            "enable": True
        },
        "level": {
            "discord": "INFO",
            "vocard": "INFO",
            "ipc_client": "INFO"
        },
        "max-history": 30
    },
    "bot_access_user": [],
    "embed_color":"0xb3b3b3",
    "default_max_queue": 1000,
    "lyrics_platform": "lrclib",
    "ipc_client": {
        "host": "127.0.0.1",
        "port": 8000,
        "password": os.getenv("IPC_PASSWORD"),
        "secure": False,
        "enable": False
    },
    "sources_settings": {},  # unchanged, auto-filled inside bot
    "default_controller": {},
    "default_voice_status_template": "{{@@track_name@@ != 'None' ?? @@track_source_emoji@@ Now Playing: @@track_name@@ // Waiting for song requests}}",
    "cooldowns": {
        "connect": [2, 30],
        "playlist view": [1, 30]
    },
    "aliases": {
        "connect": ["join"],
        "leave": ["stop", "bye"],
        "play": ["p"],
        "view": ["v"]
    }
}

with open("settings.json", "w") as f:
    json.dump(settings, f, indent=4)

print("✔ settings.json generated successfully!")
