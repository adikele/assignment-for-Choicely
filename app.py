from flask import Flask
from flask import redirect, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/saved_ok")
def saved_ok():
    return render_template("saved_ok.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/save", methods=["POST"])
def save():
    '''Saves in the database key-value pair entered via URL parameters
    '''
    tostore_string = str(request.args["key"])
    tostore_number = str(request.args["value"])
    sql = "INSERT INTO dictionary_for_choicely (stored_string,  stored_number) VALUES (:stored_string,  :stored_number)"
    result = db.session.execute(
        sql, {"stored_string": tostore_string, "stored_number": tostore_number}
    )
    db.session.commit()
    return redirect("/saved_ok")


@app.route("/save2", methods=["POST"])
def save2():
    '''Saves in the database key-value pair entered via Web page /form.html
    '''
    tostore_string = request.form["given_string"]
    tostore_number = request.form["given_number"]
    sql = "INSERT INTO dictionary_for_choicely (stored_string,  stored_number) VALUES (:stored_string,  :stored_number)"
    result = db.session.execute(
        sql, {"stored_string": tostore_string, "stored_number": tostore_number}
    )
    db.session.commit()
    return redirect("/saved_ok")


@app.route("/load", methods=["GET"])
def load():
    """
    Returns a value associated with a key
    Returns 404 if no value is saved for the given key 
    """
    text = str(request.args["text"])
    sql = "SELECT * FROM dictionary_for_choicely WHERE dictionary_for_choicely.stored_string = :x"
    result = db.session.execute(sql, {"x": text})
    data = result.fetchall()
    if data == []:
        abort(404)
    return render_template("load.html", data=data)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="404"), 404


if __name__ == "__main__":
    app.debug = True
    app.run()
