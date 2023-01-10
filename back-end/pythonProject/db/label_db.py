# 调用自定义包: db, 具体路径在run.py同目录下的文件夹中, 操作数据库
# print(__main__)
from db.sqlite3_db import DB
# from db.sqlite3_db import DB

class label_DB(DB):
    def __init__(self, db_path = 'data/code.sqlite'):
        self.db_path = db_path
        self.init_table_sql = '''
        CREATE TABLE IF NOT EXISTS "Label" ("_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "userID" VARCHAR, "label_name" VARCHAR, "label_intro" VARCHAR);
        '''
        super(label_DB, self).__init__(self.db_path, self.init_table_sql)
    
    def selectOneUserdetail(self, userID):
        self.cursor.execute("SELECT userID, label_name, label_intro FROM Label WHERE userID = '{}'".format(userID))
        outs = self.cursor.fetchall()
        return outs
    
    def selectOneUserlist(self, userID):
        self.cursor.execute("SELECT label_name FROM Label WHERE userID = '{}'".format(userID))
        outs = self.cursor.fetchall()
        return outs

    def checkUserLabel(self, userID, l_name):
        self.cursor.execute("SELECT * FROM Label WHERE userID='{}' AND label_name='{}' ".format(userID,l_name))
        return self.cursor.fetchall()

    def oneUserRemoveLabel(self, userID, l_name):
        self.execute("DELETE FROM Label WHERE userID='{}' AND label_name='{}'".format(userID,l_name))

    def oneUserAddLabel(self, userID, l_name, l_intro):
        check_rst = self.checkUserLabel(userID, l_name)
        if not check_rst:
            self.execute("INSERT INTO Label (userID,label_name,label_intro) VALUES (?,?,?)",(userID, l_name, l_intro))
            return self.cursor.lastrowid
        else:
            return "existed"
    
    def oneUserModifyLabelID(self, userID, l_name, l_new):
        self.execute("UPDATE Label SET label_name='{}' WHERE userID='{}' AND label_name='{}'" .format(l_new, userID, l_name))
        return self.cursor.lastrowid
    
    def oneUserModifyLabelintro(self, userID, l_name, l_new):
        self.execute("UPDATE Label SET label_intro='{}' WHERE userID='{}' AND label_name='{}'" .format(l_new, userID, l_name))
        return self.cursor.lastrowid

    def selectAll(self):
        self.cursor.execute("SELECT * FROM Label")
        return self.cursor.fetchall()
    
    def getnumTag(self,userID):
        self.execute("SELECT num from (SELECT userID,count(userID) as num FROM Label GROUP BY userID) where userID='{}'".format(userID))
        rst = self.cursor.fetchone()
        if not rst:
            num = 0
        else:
            num = list(rst.values())[0]
        return num 

    def admin_removeUser(self, userID):
        self.execute("DELETE FROM Label WHERE userID='{}'".format(userID))

if __name__ == "__main__":
    label1 = label_DB()
    print("first print...")
    print(label1.selectAll())
    print(label1.oneUserAddLabel("admin","copy"))
    print("second print...")
    print(label1.selectAll())
    print("third print...")
    print(label1.checkUserLabel("admin","copy"))
    print("4th print...")
    print(label1.checkUserLabel("admin","copy"))
    print(label1.selectOneUser("admin"))
    
    
