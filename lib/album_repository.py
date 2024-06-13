from lib.album import Album

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    # Find a single artist by their id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"])

    # Create a new album
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                                 album.title, album.release_year, album.artist_id])
        return None

    # Delete an album by its id
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None

    # Find an album by its id
    def find(self,album_id):
        rows=self._connection.execute(
            'select * from albums where id=%s', [album_id])
        row=rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])