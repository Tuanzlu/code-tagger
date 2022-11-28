import sqlite3 as sql


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DB:
    def __init__(self, db_path='db.sqlite', init_table_sql='CREATE TABLE IF NOT EXISTS "feeds" ("_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "url" VARCHAR, "title" VARCHAR);'):
        self.con = sql.connect(db_path, check_same_thread=False)
        self.con.row_factory = dict_factory
        self.con.execute(init_table_sql)
        self.con.commit()
        self.cursor = self.con.cursor()

    def execute(self, sql, param=()):
        self.cursor.execute(sql, param)
        self.con.commit()
        # self.close()

    def close(self):
        self.con.close()

    def insert(self, url, title):
        self.execute("INSERT INTO feeds (url,title) VALUES (?,?)", (url, title))
        return self.cursor.lastrowid

    def delete(self, id):
        self.execute("DELETE FROM feeds WHERE _id = {}".format(id))

    def selectall(self, where='1=1'):
        self.cursor.execute("SELECT * FROM feeds WHERE {}".format(where))
        return self.cursor.fetchall()

    def selectone(self, where='1=1'):
        self.cursor.execute("SELECT * FROM feeds WHERE {}".format(where))
        return self.cursor.fetchone()
        self.close()

