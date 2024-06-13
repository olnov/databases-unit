from lib.user import User

"""
Constructs with
    id, username, email
"""

def test_user_construct():
    user=User(1,'joshglasson','glasson@gmail.com')
    assert user.id==1
    assert user.username=="joshglasson"
    assert user.email=="glasson@gmail.com"

"""
Test equality
"""

def test_users_equality():
    user_1=User(1,'joshglasson','glasson@gmail.com')
    user_2=User(1,'joshglasson','glasson@gmail.com')
    assert user_1==user_2

