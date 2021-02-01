from youtube_api import YouTubeDataAPI
from pytube import YouTube
import os
from dotenv import load_dotenv
from cambio import Rename_music


load_dotenv()
key = os.getenv('API_KEY')


def run():

    yt = YouTubeDataAPI(key)
    y_id = 'PL3dgJQMuT7qm9L0BqreqIG9uzYi0pihJg'
    videos = yt.get_videos_from_playlist_id(y_id)
    playlist = list()
    path = '/home/ltisoy/Music/music'

    # obtener las url de los videos de la playlist
    for i in videos:
        id_video = i['video_id']
        playlist.append(f"https://www.youtube.com/watch?v={id_video}")

    # descargar el audio
    for video in playlist:
        video_info = YouTube(video)
        video_info.streams.filter(
            only_audio=True).first().download(output_path=path)
        print(f'{video_info.title} descargado')


if __name__ == '__main__':
    
    run()

    r_music = Rename_music()
    r_music.rename_music()
