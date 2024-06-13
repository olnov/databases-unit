from lib.post import Post

"""
Constructs with
    id, title, content, views, user_id
"""

def test_post_construct():
    post=Post(1,'Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1)
    assert post.id==1
    assert post.title=="Day 1 at Makers Academy"
    assert post.content=="Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with"
    assert post.views==55
    assert post.user_id==1

"""
Test equality
"""

def test_post_equality():
    post_1=Post(1,'Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1)
    post_2=Post(1,'Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1)
    assert post_1==post_2

