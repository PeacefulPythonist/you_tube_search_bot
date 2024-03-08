
from api_keys import MAIN_BOT, TEST_BOT, ADMIN_ID


TEST_MODE = True

if TEST_MODE:
    MAIN_BOT = TEST_BOT

BOT_URL = f"https://api.telegram.org/bot{MAIN_BOT}/"

UPDATE_URL = BOT_URL + "getUpdates"
SEND_MESSAGE = BOT_URL + "sendMessage"


if __name__ == "__main__":
	print(UPDATE_URL)