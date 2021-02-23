import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# sends user to landing page
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipe.html", recipes=recipes)


@app.route("/breakfast")
def breakfast():
    recipes = list(mongo.db.recipes.find())
    return render_template("breakfast.html", recipes=recipes)


@app.route("/lunch")
def lunch():
    recipes = list(mongo.db.recipes.find())
    return render_template("lunch.html", recipes=recipes)


@app.route("/dinner")
def dinner():
    recipes = list(mongo.db.recipes.find())
    return render_template("dinner.html", recipes=recipes)


@app.route("/dessert")
def dessert():
    recipes = list(mongo.db.recipes.find())
    return render_template("dessert.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if session["user"]:
        recipes = list(mongo.db.recipes.find(
            {'created_by': session.get('user')}))

    return render_template(
        "profile.html", user=user, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name":  request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "prep_min_hour": request.form.get("prep_min_hour"),
            "prep_time": request.form.get("prep_time"),
            "cooking_min_hour": request.form.get("cooking_min_hour"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added Successfully")
        return redirect(url_for("get_recipes"))

    cooking_mins_hours = mongo.db.cooking_mins_hours.find().sort(
        "cooking_min_hour", 1)
    prep_mins_hours = mongo.db.prep_mins_hours.find().sort(
        "prep_min_hour", 1)
    categories = mongo.db.categories.find().sort(
        "category_name", 1)
    return render_template(
        "add_recipe.html", categories=categories,
        prep_mins_hours=prep_mins_hours,
        cooking_mins_hours=cooking_mins_hours)


@app.route("/edit_recipe/<recipe_id>", methods=["POST", "GET"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name":  request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "prep_min_hour": request.form.get("prep_min_hour"),
            "prep_time": request.form.get("prep_time"),
            "cooking_min_hour": request.form.get("cooking_min_hour"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Updated Successfully")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cooking_mins_hours = mongo.db.cooking_mins_hours.find().sort(
        "cooking_min_hour", 1)
    prep_mins_hours = mongo.db.prep_mins_hours.find().sort("prep_min_hour", 1)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories,
        prep_mins_hours=prep_mins_hours, cooking_mins_hours=cooking_mins_hours)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():

    if request.method == "POST":

        today_date = date.today()
        current_date = today_date.strftime("%d %b %y")
        add_review = {
            "username": session["user"],
            "recipe_rating": request.form.get("recipe_rating"),
            "recipe_review": request.form.get("recipe_review"),
            "review_date": current_date
        }
        mongo.db.reviews.insert_one(add_review)

        flash("Review Added")
        return redirect(url_for("get_recipes"))

    return render_template("add_review.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
