
from youtube_api import YouTubeDataAPI
from pytube import YouTube
import os
from dotenv import load_dotenv
from cambiar_nombre import Rename_music
import logging

logging.basicConfig(filename="musica.log", level=logging.INFO)

load_dotenv()
key = os.getenv('API_KEY')


def run():

    yt = YouTubeDataAPI(key)
    y_id = input('Insertar Id: ')
    videos = yt.get_videos_from_playlist_id(y_id)
    playlist = list()
    path = '/home/ltisoy/Music/music'

    # obtener las url de los videos de la playlist
    for i in videos:
        id_video = i['video_id']
        playlist.append(f"https://www.youtube.com/watch?v={id_video}")

    # descargar el audio
    contador = 0
    for video in playlist:
        video_info = YouTube(video)
        try:
            video_info.streams.filter(
                only_audio=True).first().download(output_path=path)
            print(f'{video_info.title} descargado')
           #logging.info(f'{video_info.title} descargado')
            contador += 1
        except:
            logging.error(f'{video_info.title} No descargado')

    print("_________________________")
    print(f"{contador} canciones descargadas")
    print("_________________________")


if __name__ == '__main__':
    logging.info("---- iniciando descargas ----")
    run()

    r_music = Rename_music()
    r_music.rename_music()
