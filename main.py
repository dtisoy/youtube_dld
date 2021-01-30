from youtube_api import YouTubeDataAPI
from pytube import YouTube
 
key = 'AIzaSyAWJ-XQ2zKMccIjCxgjfV-KvtzAz8lfi3Y'
yt = YouTubeDataAPI(key)
y_id = input('id: ')
videos = yt.get_videos_from_playlist_id(y_id)
playlist = list()


for i in videos:
    id_video = i['video_id']
    playlist.append(f"https://www.youtube.com/watch?v={id_video}")

for video in playlist:
    yt = YouTube(video)
    print(yt.title)

# def _video_url(watch_path: str):
#         return f"https://www.youtube.com{watch_path}"
# self.playlist_url = (
#             f"https://www.youtube.com/playlist?list={self.playlist_id}

# trim_index = videos_urls.index(f"/watch?v={until_watch_id}"
