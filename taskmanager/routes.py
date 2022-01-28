#importing the function to display html files as part of the flask route
from flask import render_template, request, redirect, url_for

from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template('tasks.html')


@app.route("/categories")
def categories():
    #Flask-SQLAlchemy query to query the Category model into cursor object (iterable variable)
    #wrapped in list so that front end can deal with it, as cursor objects are tricky
    categories = list(Category.query.order_by(Category.category_name).all())
    #when a user clicks on categories link template is rendered
    #1st categories is the categories that can be used in html template
    #2nd is the categories variable in this function
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")