

from youtubesearchpython import VideosSearch

def get_yt_video_link(query):
    videosSearch = VideosSearch(query, limit=3)
    result= videosSearch.result()
    video_title=[video['title'] for video in result['result']]
    video_link=[video['link'] for video in result['result']]
    return video_title, video_link



