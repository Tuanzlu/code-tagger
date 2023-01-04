# 调用自定义包: db, 具体路径在run.py同目录下的文件夹中, 操作数据库
# print(__main__)
from db.sqlite3_db import DB
# from db.sqlite3_db import DB

class code_DB(DB):
    def __init__(self, db_path = 'data/code.sqlite'):
        self.db_path = db_path
        self.init_table_sql = '''
        CREATE TABLE IF NOT EXISTS "Code" ("_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "userID" VARCHAR, "code" VARCHAR, "code_name" VARCHAR);
        '''
        super(code_DB, self).__init__(self.db_path, self.init_table_sql)
    
    def selectOneUser(self, userID):
        self.cursor.execute("SELECT userID, code, code_name FROM Code WHERE userID = '{}'".format(userID))
        outs = self.cursor.fetchall()
        return outs

    def checkUserCode(self, userID, c_name):
        self.cursor.execute("SELECT * FROM Code WHERE userID='{}' AND code_name='{}'".format(userID,c_name))
        return self.cursor.fetchall()

    def oneUserRemoveCode(self, userID, c_name):
        self.execute("DELETE FROM Code WHERE userID='{}' AND code_name='{}'".format(userID,c_name))

    def oneUserAddCode(self, userID, c, c_name):
        check_rst = self.checkUserCode(userID, c_name)
        if not check_rst:
            self.execute("INSERT INTO Code (userID,code,code_name) VALUES (?,?,?)",(userID, c, c_name))
            return self.cursor.lastrowid
        else:
            return "existed"

    def selectAll(self):
        self.cursor.execute("SELECT * FROM Code")
        return self.cursor.fetchall()

    def oneUserModifyCodeID(self, userID, c_name, c_name_new):
        check_rst = self.checkUserCode(userID, c_name)
        if not check_rst:
            self.execute("UPDATE Code SET code_name='{}' WHERE userID='{}' AND code_name='{}'".format(c_name_new, userID, c_name))
            return self.cursor.lastrowid
        else:
            return "existed"

    def oneUserModifyCode(self, userID, c_name, c_new):
        self.execute("UPDATE Code SET code='{}' WHERE userID='{}' AND code_name='{}'".format(c_new, userID, c_name))
        return self.cursor.lastrowid

    def selectOneCode(self, userID,c_name):
        self.cursor.execute("SELECT userID, code, code_name FROM Code WHERE userID = '{}' AND code_name='{}'".format(userID,c_name))
        outs = self.cursor.fetchall()
        return outs

if __name__ == "__main__":
    code1 = code_DB()
    print("first print...")
    print(code1.selectAll())
    print(code1.oneUserAddCode("admin","www.baidu.com","baidu"))
    print("second print...")
    print(code1.selectAll())
    print("third print...")
    print(code1.checkUserCode("admin", "baidu"))
    #print(code1.checkUserCode("admin",'www.baidu.com',"baidu"))
    print("4th print...")
    print(code1.checkUserCode("admin", "baidu"))
    #print(code1.checkUserCode("admin",'www.360.com',"baidu"))
    print(code1.selectOneUser("admin"))
    
    