# 调用自定义包: db, 具体路径在run.py同目录下的文件夹中, 操作数据库
from db.sqlite3_db import DB


class user_DB(DB):
    def __init__(self, db_path='data/user.sqlite'):
        self.db_path = db_path
        self.init_table_sql = '''
        CREATE TABLE IF NOT EXISTS "users" ("_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "username" VARCHAR, "passwd" VARCHAR, "telphone" VARCHAR);
        '''
        super(user_DB, self).__init__(self.db_path, self.init_table_sql)

    def addUser(self, username, passwd, telphone):
        self.execute("INSERT INTO users (username,passwd,telphone) VALUES (?,?,?)", (username, passwd, telphone))
        return self.cursor.lastrowid

    def selectAllUser(self):
        self.cursor.execute("SELECT * FROM users WHERE username != 'admin'")
        return self.cursor.fetchall()

    def removeUser(self, username, passwd, telphone):
        self.execute("DELETE FROM users WHERE username='{}' AND passwd='{}' AND telphone='{}'".format(username, passwd, telphone))

    def GetSameTelphone(self, telphone):
        self.cursor.execute("SELECT * FROM users WHERE telphone='{}'".format(telphone))
        return self.cursor.fetchone()

    def GetLoginInfo(self, telphone):
        self.cursor.execute("SELECT passwd FROM users WHERE telphone='{}'".format(telphone))
        return self.cursor.fetchone()

    def checkUser(self, username, passwd, telphone):
        self.cursor.execute("SELECT * FROM users WHERE username='{}' AND passwd='{}' AND telphone='{}'".format(username, passwd, telphone))
        return self.cursor.fetchone()

    def GetSameUsername(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username='{}'".format(username))
        return self.cursor.fetchone()

    def updatePassword(self, telphone, passwd):
        self.cursor.execute("UPDATE users SET passwd='{}' WHERE telphone='{}'".format(passwd, telphone))
        return self.cursor.fetchone()

    def GetAdminPassword(self):
        self.cursor.execute("SELECT passwd FROM users WHERE username = 'admin'")
        return self.cursor.fetchone()

    def admin_removeUser(self, username):
        self.execute("DELETE FROM users WHERE username='{}'".format(username))


if __name__ == "__main__":
    userdb = user_DB()
    print("first print...")
    print(userdb.selectAllUser())
    userdb.addUser("admin", "123456", "11111111111")
    print("second print...")
    print(userdb.selectAllUser())
