from lib.user import User
from lib.user_repository import UserRepository

"""
When we call User all method
We are able to get all the records from table Users
"""

def test_user_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=UserRepository(db_connection)
    users=repository.all()

    assert users==[
        User(1,'joshglasson','glasson@gmail.com'),
        User(2,'johnlennon','lennon@gmail.com')
    ]


"""
When we call User create method
We are able to see newly added record
"""

def test_user_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=UserRepository(db_connection)
    repository.create('paulmaccartney','maccartney@gmail.com')
    users=repository.all()
    assert users==[
        User(1,'joshglasson','glasson@gmail.com'),
        User(2,'johnlennon','lennon@gmail.com'),
        User(3,'paulmaccartney','maccartney@gmail.com')
    ]

"""
When we call User delete method 
We are able to see all records except deleted one
"""

def test_user_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=UserRepository(db_connection)
    repository.delete(3)
    users=repository.all()

    assert users==[
        User(1,'joshglasson','glasson@gmail.com'),
        User(2,'johnlennon','lennon@gmail.com')
    ]

"""
When we call User update method 
We are able to records with updated email or/and username
"""

def test_user_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=UserRepository(db_connection)
    repository.update(2,'lennon','john@gmail.com')
    users=repository.all()

    assert users==[
        User(1,'joshglasson','glasson@gmail.com'),
        User(2,'lennon','john@gmail.com')
    ]
