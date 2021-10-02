# youtube_dld

Esta aplicacion permite descargar playlist a audio (a traves del id de la playlist), con extension mp4 asi que hay que cambiar las extensiones(el programa intenta cambiar los nombres, es necesario verificar la ruta en el archivo cambiar_nombres.py).

Para usarla es necesario crear unas [credenciales para usar las apis de google](https://console.cloud.google.com/apis) y crear un nuevo proyecto que permita consumir las apis de youtube.

 - clonar el repositorio y dentrar en la carpeta del proyecto
 -  Para usar la aplicación se debe crear un archivo .env
 - dentro del archivo escribir:
 API_KEY = 'las credenciales que se crearon en la consola de google'
 - crear un entorno virtual
 - ejecutar: `pip install -r requirements`
 - `python3 main.py`
