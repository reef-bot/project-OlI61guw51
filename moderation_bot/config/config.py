Filename: moderation_bot/config/config.py

# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Discord bot token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Bot prefix for commands
BOT_PREFIX = "!"

# SQLite database file
DATABASE_FILE = "moderation_bot.db"

# Bot admin role
ADMIN_ROLE = "Admin"

# Error log file
ERROR_LOG_FILE = "error.log"

# Bot status message
STATUS_MESSAGE = "Moderating the server"

# Moderation actions
MODERATION_ACTIONS = {
    "mute": "Mute user",
    "warn": "Warn user",
    "delete_message": "Delete message"
}

# Filter settings
FILTER_SETTINGS = {
    "profanity": True,
    "spam": True,
    "caps_lock": True,
    "emojis": True
}

# User monitoring settings
USER_MONITORING_SETTINGS = {
    "track_activity": True,
    "activity_threshold": 5,
    "warning_threshold": 3
}

# Command permissions
COMMAND_PERMISSIONS = {
    "mute": "Admin",
    "warn": "Admin",
    "delete_message": "Admin"
}

# Bot response messages
RESPONSE_MESSAGES = {
    "mute_success": "User has been muted",
    "warn_success": "User has been warned",
    "delete_message_success": "Message has been deleted"
}