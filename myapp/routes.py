from flask import render_template, request
from myapp import app, mongo



@app.route("/", methods = ['GET', 'POST'])
def index():
    # Our database
    todo_collection = mongo.db.ToDoCollection
    todos = todo_collection.find({})
    if request.method == 'POST':
        if request.form['content'] != "":
            todo_collection.insert_one({"text" : request.form['content'], "complete" : False})
    return render_template("index.html", todos=todos)