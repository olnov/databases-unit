from lib.post import Post

class PostRepository:
    def __init__(self, db_connection):
        self.db_connection=db_connection

    def all(self):
        rows=self.db_connection.execute("select * from posts order by id")
        posts=[]
        for row in rows:
            item=Post(row["id"],row["title"],row["content"],row["views"],row["user_id"])
            posts.append(item)
        return posts
    
    def create(self,title,content,views,user_id):
        self.db_connection.execute("insert into posts (title,content,views,user_id) values (%s,%s,%s,%s)",
                                    [title,content,views,user_id])
        return None
    
    def delete(self,id):
        self.db_connection.execute("delete from posts where id=%s",[id])
        return None
    
    def find(self,id):
        rows=self.db_connection.execute("select * from posts where id=%s",[id])
        row=rows[0]
        return Post(row["id"],row["title"],row["content"],row["views"],row["user_id"])
    
    def update(self,post):
        self.db_connection.execute("update posts set title=%s, content=%s, views=%s, user_id=%s where id=%s",
                                    [post.title, post.content, post.views, post.user_id, post.id])
        return None