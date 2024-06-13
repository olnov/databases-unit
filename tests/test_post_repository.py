from lib.post import Post
from lib.post_repository import PostRepository

"""
When we call Post all method
We are able to get all the records from table posts
"""

def test_post_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=PostRepository(db_connection)
    posts=repository.all()

    assert posts==[
        Post(1,'Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1),
        Post(2,'Day 2 at Makers Academy','Day 2 was the day we actually started coding!',38, 1),
        Post(3,'Let it be','When I find myself in times of trouble...',6000000, 2)
    ]


# """
# When we call User create method
# We are able to see newly added record
# """

def test_post_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=PostRepository(db_connection)
    repository.create('New title','New post',1,1)
    posts=repository.all()
    assert posts==[
        Post(1,'Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1),
        Post(2,'Day 2 at Makers Academy','Day 2 was the day we actually started coding!',38, 1),
        Post(3,'Let it be','When I find myself in times of trouble...',6000000, 2),
        Post(4,'New title','New post',1,1)
    ]

"""
When we call Pots delete method 
We are able to see all records except deleted one
"""

def test_post_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=PostRepository(db_connection)
    repository.delete(4)
    posts=repository.all()
    assert posts==[
        Post(1,'Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1),
        Post(2,'Day 2 at Makers Academy','Day 2 was the day we actually started coding!',38, 1),
        Post(3,'Let it be','When I find myself in times of trouble...',6000000, 2)
    ]


"""
When we call Post find method and passing id of the record
We are able to see the exact record
"""

def test_post_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=PostRepository(db_connection)
    result=repository.find(1)
    assert result==Post(1,'Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1)
    


"""
When we call Post update method 
We are able to records with updated title/content or views
"""

def test_post_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository=PostRepository(db_connection)
    post=repository.find(1)
    post.title="Updated title"
    assert repository.update(post) is None
    posts=repository.all()
    assert posts==[
        Post(1,'Updated title','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1),
        Post(2,'Day 2 at Makers Academy','Day 2 was the day we actually started coding!',38, 1),
        Post(3,'Let it be','When I find myself in times of trouble...',6000000, 2)
    ]