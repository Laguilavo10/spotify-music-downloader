# Descarga Música de Spotify

Este proyecto es una herramienta de línea de comandos que permite descargar tus canciones guardadas de Spotify como archivos MP3. Utiliza la API de Spotify para obtener los datos de las canciones y luego descarga las canciones de YouTube. También añade metadatos a los archivos MP3, como el título de la canción, el artista, el álbum, el número de pista y la portada del álbum.

---
- [English version of this document available here.](./README.md)
---

## Cómo usar

1. Clona este repositorio en tu máquina local y accede a él:
```
git clone https://github.com/Laguilavo10/spotify-music-downloader
cd spotify-music-downloader
```

2. Crea un entorno de Python para este proyecto:
```
python -m venv venv
```

3. Activa el entorno:
    - Linux:
    ```
    source venv/Scripts/activate
    ```
    - Windows:
    ```
    .\venv\Scripts\activate
    ```

4. Instala las dependencias del proyecto.
```
pip install -r requirements.txt
```

5. Configura tus credenciales de Spotify:
  - Necesitarás un `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` y `SPOTIPY_REDIRECT_URI`.
    - Puedes obtener estos creando una aplicación en el [Dashboard de Desarrolladores de Spotify](https://developer.spotify.com/).
      - En "Redirect URI" puedes especificar por ejemplo: "https://developer.spotify.com/".
      - En "Which API/SDKs are you planning to use?", es suficiente con clickear en "Web API".
    -  Luego, añade tus credenciales a un archivo `.env` en la raíz del proyecto (Revisa el archivo ".env.example").

```
SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=
SPOTIPY_REDIRECT_URI=
```

6. Configura las rutas de guardado para la música y los vídeos en el archivo `.env`:
```
PATH_SAVE_MUSIC=
PATH_SAVE_VIDEO=
```

7. Ejecuta el script principal:
```
py main.py
```
- Se abrirá en el navegador una página web, copiar la URL de esa página y pegarla en la consola. (La primera vez solicitará permiso para que esta app se conecte a la API de Spotify)

El script descargará las canciones guardadas en tu biblioteca de Spotify, las convertirá a MP3 y añadirá los metadatos correspondientes.


## Aviso Legal y Exención de Responsabilidad

Este proyecto se ha desarrollado con fines educativos y de aprendizaje. No se recomienda ni respalda su uso para la comercialización, distribución no autorizada de música o cualquier actividad ilegal. La utilización de este proyecto está sujeta a las leyes de derechos de autor y condiciones de servicio de las plataformas involucradas, como Spotify y YouTube.

El creador y los contribuyentes de este proyecto no asumen ninguna responsabilidad por el uso indebido, ilegal o no autorizado de esta herramienta por parte de terceros. Cualquier acción tomada con base en el código, la información proporcionada o las funcionalidades de este proyecto se realiza bajo la responsabilidad individual del usuario.

Además, se exime de cualquier responsabilidad derivada de daños, pérdidas o consecuencias legales que puedan surgir por el uso de este software de manera inapropiada o en violación de los términos y condiciones establecidos por las plataformas de terceros involucradas.

Por lo tanto, al utilizar este proyecto, el usuario acepta plenamente la responsabilidad de cumplir con todas las leyes y regulaciones aplicables y utilizarlo únicamente de acuerdo con los términos de servicio de las plataformas pertinentes y la legislación vigente en su jurisdicción.

