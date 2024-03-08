""""
tgbot.py: This file contains functions for interacting with the Telegram bot, such as sending messages and handling updates.
"""
import sys
import traceback

from requests import get, post

from consts import BOT_URL, UPDATE_URL, SEND_MESSAGE, TEST_MODE, ADMIN_ID


def send_message(text, message=ADMIN_ID):
    """send_message(text, message=ADMIN_ID): Sends a message to a specified user or chat."""
    if isinstance(message, dict):
        message_id = message['chat']['id']
    else:
        message_id = message

    url = SEND_MESSAGE
    params = {
        'chat_id': message_id,
        "text": text,
    }

    response = post(url, json=params)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to send message. Status code:", response.status_code)
        print(response.text)

    return response.json()


def get_updates():
    """get_updates(): Retrieves updates from the Telegram bot."""
    response = get(UPDATE_URL)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get updates. Status code:", response.status_code)
        print(response.text)


def send_hello(message):
    """send_hello(message): Sends an introductory message to the user."""
    text = "Please send me the words you want to search on YouTube, and I'll provide you with the search results. If you share a playlist link, I'll send you the videos from it. Alternatively, if you want all the videos from a channel, just share any video from that channel with me."
    send_message(text, message)

def send_links(links, user_id=None):
    """send_links(links, user_id=None): Sends a list of links to the user."""
    for link in links:
        send_message(link, user_id)


def send_error_message():
    """send_error_message(): Sends an error message to the admin in case of an exception."""
    exc_type, exc_value, exc_traceback = sys.exc_info()

    if TEST_MODE:
        # Print stack trace
        traceback.print_tb(exc_traceback)
    send_message(str(exc_type))
    send_message(str(exc_value))

    # Get formatted traceback as a list of strings
    tb_str_list = traceback.format_tb(exc_traceback)

    # Join the list of strings into a single string
    tb_str = '\n'.join(tb_str_list)
    send_message(tb_str)


def set_webhook(server_url=None):
    """set_webhook(server_url=None): Sets the webhook for the Telegram bot (used in AWS Lambda)."""
    url = BOT_URL + "setWebhook"
    params = {
        "url": server_url
    }

    response = post(url, json=params)

    if response.status_code != 200:
        print("Failed to send message. Status code:", response.status_code)
        print(response.text)


if __name__ == "__main__" and not TEST_MODE:
    set_webhook(

    )