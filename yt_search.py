"""
yt_search.py: Functions for searching YouTube and retrieving video links.

Functions:
- get_serch_result(text): Searches YouTube for videos and returns their links.
- get_playlist_videos(url): Retrieves video links from a YouTube playlist.
- get_channel_videos(link: str): Retrieves video links from a YouTube channel.
"""

from youtubesearchpython import VideosSearch
from youtubesearchpython import Video, ResultMode
from youtubesearchpython import Playlist, playlist_from_channel_id


def get_serch_result(text):
    """Qiduruvda topilgan viodeo linklarini qaytaruvchi funksiya"""
    search = VideosSearch(text, limit=20)
    result = search.result()["result"]
    return [video["link"] for video in result]

def get_playlist_videos(url):
    """Playlist video linklarini qaytaruvchi funksiya"""

    if len(url) == 24:
        url = playlist_from_channel_id(url)
        # print("This is a channel")
    playlist = Playlist(url)
    while playlist.hasMoreVideos:
        playlist.getNextVideos()
        # print(f'Videos Retrieved: {len(playlist.videos)}')
    videos = playlist.videos
    return [video["link"] for video in videos]

def get_channel_videos(link: str):

    if "https://youtu.be/" in link:
        link = link.split("?", maxsplit=1)[0].split("/")[-1]
    # print(link)
    video = Video.getInfo(link, mode = ResultMode.json)
    # print(video, "fffffffff")
    all_video = video["channel"]["id"]
    return get_playlist_videos(all_video)
