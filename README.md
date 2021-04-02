# Limitless Recipes

Limitless Recipes is a website for users to find and upload recipes, accessible on a wide range of devices for all users.

## Table of Contents 
> - [User Stories](#user-stories)
> - [UX](#ux)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Testing](#testing)
> - [Code validity](#code-validity)
> - [Deployment](#deployment)
> - [Credits](#credits)
> - [Acknowledgments](#acknowledgments)


#### User Stories
- "As a user I want to add my own recipes to the website."
  - Using CRUD (Create) a user could input there recipe by using a form, which submitted to the database (MongoDB) then shown on the website. [Add recipe form](static/images/recipe-form.png) [Recipe in database](static/images/recipe-database.png) [Recipe shown on website](static/images/recipe-site.png)
- "As a user I want to be able to edit my recipe."
  - Using CRUD (Update) a user can edit there submitted recipes using a provided form, which updated the database (MongoDB), showing the updated version the website. [Edit recipe button](static/images/edit-recipe-button.png) [Edit recipe form](static/images/edit-recipe-form.png)
- "As a user I want to be able to delete my recipe."
  - Using CRUD (Delete) a user could delete there uploaded recipe from the database, which would then remove it from the website. [Delete recipe button](static/images/delete-recipe-form.png)
- "As a user I want to be able to easily view other users recipes."
  - Using a button on the website called 'view', it opens the specific users website into a full page to be viewed easily. [View recipe button](static/images/view-recipe-button.png) [View recipe page](static/images/view-recipe-page.png)
- "As a user I want to be able to use a search bar to find recipes."
  - Using CRUD (Read) a user can search the database (MongoDB) to find a specific recipe, it will then return results. [search bar](static/images/search-bar.png) [Search bar returned results](static/images/search-bar-results.png)
- "As a user I want to be able to create an account."
  - This is accomplished by adding a form where the user can input there details and submit into the database (MongoDB). [register page form](static/images/register-img.png) [users in database](static/images/user-database.png) [Logged in](static/images/user-loggedin.png)
- "As a user who has created an account I want to be able to login."
  - This is completed where a user can input there details previously used to sign up, which is then checked in the database (MongoDB) and is then logged in. [Log In Page](static/images/log-in-page.png) [Logged In](static/images/user-loggedin.png)
- "As a user I want to be able to write a review for a recipe."
  - This was achieved using CRUD (Create) where a user added there review and it was then submited into the database (MongoDB). [Add review button one](static/images/add-review-button-one.png) [Add review button two](static/images/add-review-button-two.png) [add review form](static/images/add-review-form.png) [add review database](static/images/review-database.png) [add review shown in website one](static/images/review-shown-one.png) [add review shown in website two](static/images/review-shown-one.png)
- "As a user I want to be able to delete my review."
  - This was done by using CRUD (Delete) which as user can delete there review only if it is theres. [review delete button one](static/images/review-delete.png)

#### Owner Stories
- "I want my users to be able to add there own recipes".
- "I want my users to be able to find/view other users recipes".
- "I want my users to be able to sign up, sign in and logout".
- "I want my users to be able to review other user recipes".
- "I want my users to be able to search for recipes".

## UX

### Project Goals
* For users to upload there recipes onto the website.
* Users to review other users recipes.
* Profile page where users can see there uploaded recipes.
* Log In/ Log out functionality.
* Ease of use.

### Scope
* Allow users to register an account on the website.
* Allow registered users to Create, Read, Update and Delete (CRUD) recipes.
* Create functionality for users to Create, Delete reviews on recipes.
* Create using my current skills, HTML, CSS, JavaScript, Python, Flask and MongoDB

### Structure
* Navigation bar located at the top of the website for ease of navigation through site.
* Logged in users to be able to use CRUD functionality with recipes.

### Skeleton
#### Wireframes

### Surface

#### Colours
I have chosen these set of colours for my website:

* #116466 
* #D1E8E2 
* #FFCB9A 
* white
* black

#### Typography
* "Lexend Mega" Used for main pecies of content like titles and headings.
* "Lato" Used for most of the text throughout the website, as it is a clean font and makes it very user-friendly and easy to read.

#### Imagery
When choosing imagery I took the websites [HERE]

## Features

### Existing Features
* Created with HTML5, CSS3, Javascript, jQuery, Materialize and MongoDB.
* Home/Index page to give the users an idea of the website with the use of imagery and text, with a call to action button to discover recipes.
* Responsive design.
* Footer with social media links.
* 'Add Recipe' page for users to create there own recipe and add it to the website.
* Reviews button which opens a form, for users to review recipes.
* Search bar for users to search the website for specific recipes.
* Profile page showing when the user signed up and the recipes they have added.

### Features Left To Implement
* A future feature that would be a good addition would be a favrioute button on recipes. This button would save the recipe in the users profile for ease of use to come back to later.

## Technologies Used

[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)

[Python](https://en.wikipedia.org/wiki/Python_(programming_language))

[Google Fonts](https://fonts.google.com/)

[jQuery](https://jquery.com/)

[Materialize](https://materializecss.com/)

[FontAwesome](https://fontawesome.com/)

[MongoDB](https://www.mongodb.com/)

[Flask](https://flask.palletsprojects.com/en/1.1.x/)

### Code validity

- HTML - [W3C](https://validator.w3.org/) - Markup Validation
- CSS - [W3C](https://jigsaw.w3.org/css-validator/) - Jigsaw CSS Validation
- JavaScript - [JSHINT](https://jshint.com/) - JavaScript code warning & error check
- Python - [Pyton Tester](https://extendsclass.com/python-tester.html) Python code syntax checker
- TAGS - [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) - Validates all tags are opening and closing correctly.

## Resources 
* Code Institute Course Content
* Youtube
* W3C
* Balsamiq
* Stack Overflow
* Code Institute Slack community

## Testing

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JackTubby/Limitless-Recipes)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
   - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com/JackTubby/Limitless-Recipes) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JackTubby/Limitless-Recipes)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JackTubby/Limitless-Recipes)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Creating Collections in MongoDB

1. Login to your MongoDB account
2. Create a **cluster**
3. Create a **database**
4. Create four **collections** in the database named:

    - **users**
    - **countries**
    - **blogs**

### Setting Up the Environment Variables
1. Create a file called **.gitignore** in the root directory of your project
2. Add the following text in your .gitignore file: **env.py**
3. Create a file called **env.py**. This will contain all your environment variables
4. Create your own personal secret key and password. In **env.py** add the following text and replace **YOURPASSWORD**, **YOUR-CLUSTER-NAME**, **YOUR-DATABASE-NAME** and **YOURSECRETKEY**    

### Run the App 
1. Open your terminal window in your IDE
2. Type in **python3 app.py** to run the app

### Heroku Deployment
1. Create a Heroku account
2. Create a new app and select your region
3. In the terminal window of your local IDE type **pip3 freeze --local > requirements.txt** to create a requirements.txt file. This file is needed so that Heroku knows which files needs to be installed
5. In the terminal window of your local IDE type **python app.py > Procfile** to create a Procfile. This file is needed so that Heroku knows which file is needed as its entry point to get the app up and running
6. In the terminal window of your local IDE type in **heroku login** or **heroku login -i** and fill in your heroku credentials and password
7. Commit all your files and type in the same terminal window **git push heroku master**. Now all your files are committed to Heroku
8. Go back to your Heroku account and go to **settings**
9. Click on **Reveal Config Vars** to reveal the keys and the values
10. Set the keys and values as follow:
    (**KEY: VALUE**)
    - IP: 0.0.0.0
    - PORT: 5000
    - MONGO_DBNAME: YOUR-DATABASE-NAME
    - MONGO_URI: mongodb+srv://root:**YOURPASSWORD**@**YOUR-CLUSTER-NAME**.2qobt.mongodb.net/**YOUR-DATABASE-NAME**?retryWrites=true&w=majority
    - SECRET_KEY: YOURSECRETKEY
11. Click on **Open app** in the right corner of your Heroku account, the application will open in a new window
12. The live link is available from the address bar

## Credits 

### Media

* [Pexels](https://www.pexels.com/) was used for imagery.

### Acknowledgements 

* My mentor for his feedback and advice throughout.
* Tutor support at Code Institute for their assistance.
* Slack community for assistance and questions.