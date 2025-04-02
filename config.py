from os import environ

def get_int_env(var_name, default=0):
    try:
        return int(environ.get(var_name, default))
    except ValueError:
        return default

API_ID = get_int_env("API_ID")
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = get_int_env("OWNER_ID")
LOG_CHANNEL = get_int_env("LOG_CHANNEL")
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")
PORT = get_int_env("PORT", 8080)

AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",") if channel_id.isdigit()]
