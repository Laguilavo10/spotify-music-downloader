# Spotify Music Download Project

This project is a command-line tool that allows you to download your saved Spotify songs as MP3 files. It uses the Spotify API to fetch song data and then downloads the songs from YouTube. It also adds metadata to the MP3 files, such as the song title, artist, album, track number, and album cover.

---
- [Versión en Español de este documento disponible aquí.](./README_ES.md)
---

## How to Use

1. Clone this repository to your local machine and then go to in it:
```
git clone https://github.com/Jonatandb/spotify-music-downloader
cd spotify-music-downloader
```

2. Create a Python environment for this project:
```
python -m venv venv
```

3. Activate the environment:
    - Linux:
    ```
    source venv/Scripts/activate
    ```
    - Windows:
    ```
    .\venv\Scripts\activate
    ```

4. Install project dependencies:
```
pip install -r requirements.txt
```

5. Set up your Spotify credentials:
  - You'll need a `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` and a `SPOTIPY_REDIRECT_URI`.
    - You can obtain these by creating an application in the [Spotify Developer Dashboard](https://developer.spotify.com/). In "Redirect URI" you can specify for example: "https://developer.spotify.com/".
    - Then, add your credentials to a `.env` file in the project root (Check ".env.example" file).

```
SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=
SPOTIPY_REDIRECT_URI=
```

6. Configure the save paths for music and videos in the `.env` file:

```
PATH_SAVE_MUSIC=
PATH_SAVE_VIDEO=
```

7. Run the main script:

```
py main.py
```
- A web page will open in the browser, copy the URL of that page and paste it into the console. (The first time it will request permission for this app to connect to the Spotify API)

The script will download the songs saved in your Spotify library, convert them to MP3, and add the corresponding metadata.

## Legal Notice and Disclaimer

This project has been developed for educational and learning purposes. Its use for commercial purposes, unauthorized distribution of music, or any illegal activities is not recommended nor endorsed. The use of this project is subject to copyright laws and terms of service of the involved platforms such as Spotify and YouTube.

The creator and contributors of this project do not assume any responsibility for the misuse, illegal, or unauthorized use of this tool by third parties. Any actions taken based on the code, information provided, or functionalities of this project are done under the individual responsibility of the user.

Furthermore, any liability arising from damages, losses, or legal consequences that may result from the inappropriate use or violation of terms and conditions set by the involved third-party platforms are hereby disclaimed.

Therefore, by using this project, the user fully accepts the responsibility to comply with all applicable laws and regulations and to use it solely in accordance with the terms of service of the relevant platforms and the prevailing legislation in their jurisdiction.


