

from base_lambda import get_message
from tgbot import send_error_message, send_links, send_hello
from yt_search import get_serch_result, get_channel_videos, get_playlist_videos


def get_links(text):
    if "list=" in text:
        return get_playlist_videos(text)
    elif "https://" in text:
        return get_channel_videos(text)
    else:
        return get_serch_result(text)

def message_processing(message):

    text = message.get('text')
    if "/start" == text:
        send_hello(message)

    user_id = message['chat']['id']
    links = get_links(text)
    send_links(links, user_id)

def main(event=None, context=None):

    message = get_message(event)
    try:
        message_processing(message)
    except Exception:
        send_error_message()
    return {
        'statusCode': 200,
    }


if __name__ == "__main__":
    main()
    # print(len("UCbOCbp5gXL8jigIBZLqMPrw"))