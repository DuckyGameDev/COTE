import os

# Use environment variables to store sensitive information and configuration settings
TG_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN', 'default_token')
TG_API_URL: str = os.getenv('TELEGRAM_API_URL', 'https://api.telegram.org/bots')