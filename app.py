import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from flask_paginate import Pagination, get_page_args
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


# --- Error Pages --- #
# Handle 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', error=error), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template("errors/500.html"), 500


# Handle 403 erros
@app.errorhandler(403)
def forbidden(e):
    return render_template("errors/403.html"), 403


# --- Recipe Pages --- #
@app.route("/get_recipes")
def get_recipes():
    # Initialize pagination
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    # Sets amount of recipes on each page
    per_page = 8
    # Adds pages for pagination
    if page == 1:
        offset = 0
    else:
        offset = (page - 1) * per_page

    # Query MongoDB (gets recipe category)
    category = request.args.get("category")
    # Gets all the recipes with the correct category
    if category:
        recipes = list(
            mongo.db.recipes.find(
                {"category_name": category}))
    # Else display all recipes
    else:
        recipes = list(mongo.db.recipes.find().sort([("_id", -1)]))
    # total number of results
    total = mongo.db.recipes.find().count()

    paginatedResults = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total)

    recipe_list = list(recipes)
    recipe_count = len(recipe_list)

    return render_template(
        "recipe.html",
        recipes=paginatedResults,
        page=page,
        per_page=per_page,
        pagination=pagination,
        total=total,
        recipe_list=paginatedResults,
        recipe_count=recipe_count)


# --- Search --- #
@app.route("/search", methods=["GET", "POST"])
def search():
    # pagination
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    # Sets amount of recipes on each page
    per_page = 8
    # Adds pages for pagination
    if page == 1:
        offset = 0
    else:
        offset = (page - 1) * per_page

    # search functionality / MongoDB query
    if "category" in request.args:

        category = request.args.get("category")
        recipes = mongo.db.recipes.find(
            {"$text": {"$search": category}})

    # finds the recipe with the query
    if "query" in request.args:
        query = request.args.get("query")
        recipes = mongo.db.recipes.find({"$text": {"$search": query}})

    # counts total of recipes
    total = mongo.db.recipes.count()

    paginatedResults = recipes[offset: offset + per_page].sort("recipe_name")
    pagination = Pagination(page=page, per_page=per_page, total=total)

    recipe_list = list(recipes)
    recipe_count = len(recipe_list)

    return render_template(
        "recipe.html",
        recipes=paginatedResults,
        page=page,
        per_page=per_page,
        pagination=pagination,
        total=total,
        recipe_list=recipe_list,
        recipe_count=recipe_count)


# --- View Recipe --- #
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    # gets selected user recipe
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # gets recipe reviews
    if "reviews" in recipe:
        reviews = list(mongo.db.reviews.find(
            {"_id": {"$in": recipe["reviews"]}}))

        return render_template(
            "view_recipe.html", recipe=recipe, reviews=reviews)

    # if no recipe redirect to get_recipes
    if not recipe:
        return redirect(url_for("get_recipes"))

    # no reviews available
    return render_template(
            "view_recipe.html", recipe=recipe)


# --- Register --- #
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # if the user exists flash message will show
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # gets to todays date
        today_date = date.today()
        current_date = today_date.strftime("%d %b %y")
        # gets form data and inserts to the db
        register = {
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "register_date": current_date,
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# --- Login --- #
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


# --- Profile --- #
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # checks user is in session
    if "user" in session:
        # Gets session user
        session_user = session["user"]
        # Checks username is equal to session user
        if username == session_user:
            page, per_page, offset = get_page_args(
                page_parameter='page', per_page_parameter='per_page')
            per_page = 4

            if page == 1:
                offset = 0
            else:
                offset = (page - 1) * per_page
            # gets recipes
            recipes = mongo.db.recipes.find()

            # grab the session user's username from the db
            user = mongo.db.users.find_one(
                {"username": session["user"]})
            # gets the recipes added by the user
            recipes = mongo.db.recipes.find(
                {'created_by': session.get('user')})
            # counts there total recipes
            total = recipes.count()

            paginatedResults = recipes[offset: offset + per_page]
            pagination = Pagination(page=page, per_page=per_page, total=total)

            return render_template(
                "profile.html",
                user=user,
                recipes=paginatedResults,
                page=page,
                per_page=per_page,
                pagination=pagination,
                total=total)
        return redirect(url_for("profile", username=session["user"]))

    return redirect(url_for("login"))


# --- Logout --- #
@app.route("/logout")
def logout():
    if "user" in session:
        # remove user from session cookies
        flash("You have been logged out")
        session.pop("user")
    return redirect(url_for("login"))


# --- Add Recipe --- #
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # checks user is in session
    if "user" in session:
        # gets form data
        if request.method == "POST":
            recipe = {
                "recipe_name":  request.form.get("recipe_name"),
                "category_name": request.form.get("category_name"),
                "recipe_description": request.form.get("recipe_description"),
                "recipe_serves": request.form.get("recipe_serves"),
                "image_url": request.form.get("image_url"),
                "prep_time": request.form.get("prep_time"),
                "cooking_time": request.form.get("cooking_time"),
                "recipe_ingredient": request.form.get("recipe_ingredient"),
                "recipe_method": request.form.get("recipe_method"),
                "created_by": session["user"]
            }
            # inserts recipe into db
            mongo.db.recipes.insert_one(recipe)
            # if added successfully it will flash this message
            flash("Recipe Added Successfully")
            # if added successfully will return to get_recipes
            return redirect(url_for("get_recipes"))
        categories = mongo.db.categories.find().sort(
            "category_name", 1)
        return render_template(
            "add_recipe.html", categories=categories)
    return redirect(url_for("login"))


# --- Edit Recipe --- #
@app.route("/edit_recipe/<recipe_id>", methods=["POST", "GET"])
def edit_recipe(recipe_id):
    # Checks user is logged in
    if "user" in session:
        # Gets session user
        session_user = session["user"]
        # Gets recipe ID
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        # Checks recipe creator is same as session user
        if recipe["created_by"] == session_user:
            if request.method == "POST":
                submit = {
                    "recipe_name":  request.form.get("recipe_name"),
                    "category_name": request.form.get("category_name"),
                    "recipe_description": request.form.get(
                        "recipe_description"),
                    "recipe_serves": request.form.get("recipe_serves"),
                    "image_url": request.form.get("image_url"),
                    "prep_time": request.form.get("prep_time"),
                    "cooking_time": request.form.get("cooking_time"),
                    "recipe_ingredient": request.form.getlist(
                        "recipe_ingredient"),
                    "recipe_method": request.form.getlist("recipe_method"),
                    "created_by": session["user"]
                }
                # updates recipe in db
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
                # if edit is successfull flash this message
                flash("Recipe Updated Successfully")
                return redirect(url_for("profile", username=session["user"]))
            categories = mongo.db.categories.find().sort("category_name", 1)
            return render_template(
                "edit_recipe.html", recipe=recipe, categories=categories)
        return redirect(url_for("get_recipes"))

    return redirect(url_for("login"))


# --- Delete Recipe --- #
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # checks user is in session
    if "user" in session:
        # Gets session user
        session_user = session["user"]
        # Gets recipe ID
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        # Checks recipe creator is same as session user
        if recipe["created_by"] == session_user:
            # removes recipe in db
            mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
            # if recipe is deleted will flash this message
            flash("Recipe Deleted")
            return redirect(url_for("profile", username=session["user"]))
        return redirect(url_for("get_recipes"))
    return redirect(url_for("login"))


# --- Add Review --- #
@app.route("/add_review/<recipe_id>", methods=["GET", "POST"])
def add_review(recipe_id):
    if "user" in session:
        # Gets session user
        session_user = session["user"]
        # Gets recipe ID
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        # Checks recipe creator is same as session user
        if recipe["created_by"] != session_user:
            if request.method == "POST":
                # gets the date
                today_date = date.today()
                current_date = today_date.strftime("%d %b %y")
                # gets form data
                add_review = {
                    "username": session["user"],
                    "recipe_rating": request.form.get("recipe_rating"),
                    "recipe_review": request.form.get("recipe_review"),
                    "review_date": current_date
                }
                # inserts data into db
                review = mongo.db.reviews.insert_one(add_review)
                review_id = review.inserted_id
                # push review ID to recipe collection as an array in the recipe
                mongo.db.recipes.update(
                    {"_id": ObjectId(recipe_id)}, {
                        "$push": {"reviews": ObjectId(review_id)}})
                # if review added flash this image
                flash("Review Added")
                return redirect(url_for("get_recipes"))
            return render_template(
                "add_review.html", recipe_id=recipe_id)
        return redirect(url_for("profile", username=session["user"]))
    return redirect(url_for("login"))


# --- Delete Review --- #
@app.route("/delete_review/<recipe_id>/<review_id>")
def delete_review(recipe_id, review_id):
    # check user is logged in
    if "user" in session:
        # Gets session user
        session_user = session["user"]
        print(session_user, "SESSION HERE")
        # Gets review ID
        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        print(review, "REVIEW HERE")
        # Checks review creator is same as session user
        if review["username"] == session_user:
            # removes from recipe collection
            mongo.db.recipes.find_one_and_update(
                {"_id": ObjectId(recipe_id)},
                {"$pull": {"reviews": ObjectId(review_id)}})
            # remove from review collection
            mongo.db.reviews.remove({"_id": ObjectId(review_id)})
            # when review deleted flash message
            flash("Review Deleted")
            return redirect(url_for("get_recipes"))
        return redirect(url_for("get_recipes"))
    return redirect(url_for("login"))


# --- Run the app --- #
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
