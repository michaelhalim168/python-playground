import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import ClientInfo

date = input("Please enter a date (YYYY-MM-DD): ")

BILLBOARD_WEBSITE = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(BILLBOARD_WEBSITE)
top_100_data = response.text

soup = BeautifulSoup(top_100_data, 'html.parser')
song_data = soup.find_all("span", {"class": "chart-element__information__song"})
artist_data = soup.find_all("span", {"class": "chart-element__information__artist"})

songs = [song.getText() for song in song_data]
artists = [artist.getText() for artist in artist_data]

client_info = ClientInfo()
CLIENT_ID = client_info.client_id
CLIENT_SECRET = client_info.client_secret

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://test.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uri = []
year = date.split('-')[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f"{song} does not exist. The track is skipped")

playlist = sp.user_playlist_create(user=user_id, name=f'{date} - Top 100 Billboard Playlist', public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uri)

