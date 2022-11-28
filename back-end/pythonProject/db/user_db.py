# 调用自定义包: db, 具体路径在run.py同目录下的文件夹中, 操作数据库
from db.sqlite3_db import DB


class UserDB(DB):
    def __init__(self, db_path='data/user.sqlite'):
        self.db_path = db_path
        self.init_table_sql = '''
        CREATE TABLE IF NOT EXISTS "users" ("_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "username" VARCHAR, "passwd" VARCHAR);
        '''
        super(UserDB, self).__init__(self.db_path, self.init_table_sql)

    def addUser(self, user, passwd):
        self.execute("INSERT INTO users (username,passwd) VALUES (?,?)", (user, passwd))
        return self.cursor.lastrowid

    def selectAllUser(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()


if __name__ == "__main__":
    userdb = UserDB()
    print("first print...")
    print(userdb.selectAllUser())
    userdb.addUser("admin", "123456")
    print("second print...")
    print(userdb.selectAllUser())
