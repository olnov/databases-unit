from lib.user import User

class UserRepository:
    def __init__(self,db_connection):
        self.db_connection=db_connection

    def all(self):
        rows=self.db_connection.execute("select * from users")
        users=[]
        for row in rows:
            item=User(row["id"],row["username"],row["email"])
            users.append(item)
        return users
    
    def create(self,username,email):
        self.db_connection.execute("insert into users (username,email) values (%s,%s)",[username,email])
        return None
    
    def delete(self,id):
        self.db_connection.execute("delete from users where id=%s",[id])
        return None
    
    def update(self,id,username,email):
        self.db_connection.execute("update users set username=%s, email=%s where id=%s",[username,email,id])
        return None