from lib.album import Album
from lib.album_repository import AlbumRepository

"""
Constructs with
    id, title, release_year, artist_id
"""

def test_album_returns_record():
    album=Album(2,"Surfer Rosa",1988,1)
    assert album.id==2
    assert album.title=="Surfer Rosa"
    assert album.release_year==1988
    assert album.artist_id==1

"""
Test equality
"""

def test_albums_equality():
    album_1=Album(2,"Surfer Rosa",1988,1)
    album_2=Album(2,"Surfer Rosa",1988,1)
    assert album_1==album_2


"""
When we call all
We get all the albums back as instances
"""

def test_all(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository=AlbumRepository(db_connection)
    result=repository.all()
    assert result==[
       Album (1,'Doolittle', 1989, 1),
       Album (2,'Surfer Rosa', 1988, 1),
       Album (3,'Waterloo', 1974, 2),
       Album (4,'Super Trouper', 1980, 2),
       Album (5,'Bossanova', 1990, 1),
       Album (6,'Lover', 2019, 3),
       Album (7,'Folklore', 2020, 3),
       Album (8,'I Put a Spell on You', 1965, 4),
       Album (9,'Baltimore', 1978, 4),
       Album (10,'Here Comes the Sun', 1971, 4),
       Album (11,'Fodder on My Wings', 1982, 4),
       Album (12,'Ring Ring', 1973, 2),
    ]