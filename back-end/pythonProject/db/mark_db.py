# 调用自定义包: db, 具体路径在run.py同目录下的文件夹中, 操作数据库
# print(__main__)
from sqlite3_db import DB
# from db.sqlite3_db import DB

class mark_DB(DB):
    def __init__(self, db_path = 'data/code.sqlite'):
        self.db_path = db_path
        self.init_table_sql = '''
        CREATE TABLE IF NOT EXISTS "Mark" ("_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "userID" VARCHAR, "codeID" VARCHAR, "lineno" INTEGER, "labelID" VARCHAR);
        '''
        super(mark_DB, self).__init__(self.db_path, self.init_table_sql)
    
    def selectOneUser(self, userID):
        self.cursor.execute("SELECT userID, codeID, lineno, labelID FROM Mark WHERE userID = '{}'".format(userID))
        outs = self.cursor.fetchall()
        return outs

    def checkUserMark(self, userID, c, line, l):
        self.cursor.execute("SELECT * FROM Code WHERE userID='{}' AND codeID='{}'  AND lineno='{}' AND labelID='{}'".format(userID,c,line,l))
        return self.cursor.fetchall()

    def oneUserRemoveMark(self, userID, c, line, l):
        self.execute("DELETE FROM Code WHERE userID='{}' AND codeID='{}'  AND lineno='{}' AND labelID='{}'".format(userID,c,line,l))

    def oneUserAddMark(self, userID, c, line, l):
        check_rst = self.checkUserMark(userID, c, line, l)
        if not check_rst:
            self.execute("INSERT INTO Code (userID,codeID,lineno,labelID) VALUES (?,?,?,?)",(userID, c, line, l))
            return self.cursor.lastrowid
        else:
            return "existed"

    def selectAll(self):
        self.cursor.execute("SELECT * FROM Code")
        return self.cursor.fetchall()

if __name__ == "__main__":
    mark1 = mark_DB()
    print("first print...")
    print(mark1.selectAll())
    
    