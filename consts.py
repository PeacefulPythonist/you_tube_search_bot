"""
consts.py: Constants and configuration settings for the project.

Variables:
- TEST_MODE (bool): Flag indicating whether the project is in test mode.
- MAIN_BOT (str): Telegram bot token (used in AWS Lambda).
- BOT_URL (str): Telegram bot URL for API requests.
- UPDATE_URL (str): URL for getting updates from Telegram.
- SEND_MESSAGE (str): URL for sending messages via Telegram.
"""

from api_keys import MAIN_BOT, TEST_BOT, ADMIN_ID


TEST_MODE = True

if TEST_MODE:
    MAIN_BOT = TEST_BOT

BOT_URL = f"https://api.telegram.org/bot{MAIN_BOT}/"

UPDATE_URL = BOT_URL + "getUpdates"
SEND_MESSAGE = BOT_URL + "sendMessage"


if __name__ == "__main__":
	print(UPDATE_URL)
