filename: settings.py

# settings for the moderation bot

# Discord API token
DISCORD_TOKEN = "your_discord_token_here"

# Bot prefix for commands
BOT_PREFIX = "!"

# Database settings
DATABASE_NAME = "moderation_bot.db"
DATABASE_TABLE = "moderation_logs"

# Error log file
ERROR_LOG_FILE = "error.log"

# Moderation settings
MESSAGE_FILTER_ENABLED = True
USER_MONITORING_ENABLED = True
WARNING_SYSTEM_ENABLED = True

# Command permissions
BOT_OWNER_ID = "your_discord_user_id_here"
ADMIN_ROLE_NAME = "Admin"
MODERATOR_ROLE_NAME = "Moderator"