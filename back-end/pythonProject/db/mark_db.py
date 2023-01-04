# 调用自定义包: db, 具体路径在run.py同目录下的文件夹中, 操作数据库
# print(__main__)
from db.sqlite3_db import DB
# from db.sqlite3_db import DB

class mark_DB(DB):
    def __init__(self, db_path = 'data/code.sqlite'):
        self.db_path = db_path
        self.init_table_sql = '''
        CREATE TABLE IF NOT EXISTS "Mark" ("_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "userID" VARCHAR, "codeID" VARCHAR, "code" VARCHAR, "labelID" VARCHAR);
        '''
        super(mark_DB, self).__init__(self.db_path, self.init_table_sql)
    
    def selectOneUser(self, userID):
        self.cursor.execute("SELECT userID, codeID, code, labelID FROM Mark WHERE userID = '{}'".format(userID))
        outs = self.cursor.fetchall()
        return outs
    
    def selectOneLabel(self, userID, labelID):
        self.cursor.execute("SELECT userID, codeID, code, labelID FROM Mark WHERE userID = '{}' AND labelID = '{}'".format(userID,labelID))
        outs = self.cursor.fetchall()
        return outs

    def checkUserMark(self, userID, c, co, l):
        self.cursor.execute("SELECT * FROM Mark WHERE userID='{}' AND codeID='{}' AND code='{}' AND labelID='{}'".format(userID,c,co,l))
        return self.cursor.fetchall()

    def oneUserRemoveMark(self, userID, c, co, l):
        self.execute("DELETE FROM Mark WHERE userID='{}' AND codeID='{}'  AND code='{}' AND labelID='{}'".format(userID,c,co,l))

    def oneUserAddMark(self, userID, c, co, l):
        check_rst = self.checkUserMark(userID, c, co, l)
        if not check_rst:
            self.execute("INSERT INTO Mark (userID,codeID,code,labelID) VALUES (?,?,?,?)",(userID, c, co, l))
            return self.cursor.lastrowid
        else:
            return "existed"
    
    def oneUserModifyLabelID(self, userID, l_name, l_new):
        self.execute("UPDATE Mark SET labelID='{}' WHERE userID='{}' AND labelID='{}'" .format(l_new, userID, l_name))
        return self.cursor.lastrowid
    
    def oneUserModifycodeID(self, userID, c_name, c_new):
        self.execute("UPDATE Mark SET codeID='{}' WHERE userID='{}' AND codeID='{}'" .format(c_new, userID, c_name))
        return self.cursor.lastrowid

    def selectAll(self):
        self.cursor.execute("SELECT * FROM Code")
        return self.cursor.fetchall()

if __name__ == "__main__":
    mark1 = mark_DB()
    print("first print...")
    print(mark1.selectAll())
    
    
