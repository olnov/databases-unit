# file: app.py

from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
    print(f"What woulld you like to do?")
    print(f"1 - Get the list of albums")
    print(f"2 - Get the list of artists")
    print (f"3 - Exit application")
    choice=input(f"Enter your coice:")
    if choice=="1":
        album_repository=AlbumRepository(self._connection)
        albums=album_repository.all()
        for album in albums:
            print (f"{album.id} - {album.title}")
    elif choice=="2":
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        for artist in artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")
    elif choice=="3":
        exit()

if __name__ == '__main__':
    app = Application()
    while app:
        app.run()
