# coding=UTF-8
from flask import Flask
from app import app
@app.route("/") #装饰器，url，路由
def index(): #试图函数
    return "hello world"
if __name__ == "__main__":
    app.run()