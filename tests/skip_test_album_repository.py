from lib.album_repository import AlbumRepository
# from lib.database_connection import DatabaseConnection as db_connection
from lib.album import Album

"""
Given album id=2
Find method returns 2 Surfer Rosa 1988 1
"""

def test_find_by_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository=AlbumRepository(db_connection)
    result=repository.find(2)
    assert result==Album(2, 'Surfer Rosa', 1988, 1)
