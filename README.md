# Limitless Recipes
<span id="recipes"></span>

Limitless Recipes is a website for users to find and upload recipes, accessible on a wide range of devices for all users.

## Table of Contents 
> - [User Stories](#user-stories)
> - [Owner Stories](#owner-stories)
> - [UX](#ux)
>   - [Project Goals](#project-goals)
>   - [Design](#design)
>   - [Information Architecture](#ia)
>   - [Wireframes](#wireframes)
> - [Features](#features)
>   - [Existing Features](#e-features)
>   - [Future Features](#f-features)
> - [Technologies Used](#technologies-used)
> - [Testing](#testing)
> - [Deployment](#deployment)
> - [Resources](#resources)
> - [Credits](#credits)
  > - [Acknowledgments](#acknowledgments)
> - [Support](#support)

<span id="user-stores"></span>

#### User Stories 
- "As a user I want to add my own recipes to the website."
  - Using CRUD (Create) a user could input there recipe by using a form, which submitted to the database (MongoDB) then shown on the website. [Add recipe form](readme_img/recipe-form.PNG) [Recipe shown on website](readme_img/recipe-site.PNG)
- "As a user I want to be able to edit my recipe."
  - Using CRUD (Update) a user can edit there submitted recipes using a provided form, which updated the database (MongoDB), showing the updated version the website. [Edit recipe button](readme_img/edit-recipe-button.PNG) [Edit recipe form](readme_img/edit-recipe-form.PNG)
- "As a user I want to be able to delete my recipe."
  - Using CRUD (Delete) a user could delete there uploaded recipe from the database, which would then remove it from the website. [Delete recipe button](readme_img/delete-recipe-form.PNG)
- "As a user I want to be able to easily view other users recipes."
  - Using a button on the website called 'view', it opens the specific users website into a full page to be viewed easily. [View recipe button](readme_img/view-recipe-button.PNG) [View recipe page](readme_img/view-recipe-page.PNG)
- "As a user I want to be able to use a search bar to find recipes."
  - Using CRUD (Read) a user can search the database (MongoDB) to find a specific recipe, it will then return results. [search bar](readme_img/search-bar.PNG) [Search bar returned results](readme_img/search-bar-results.PNG)
- "As a user I want to be able to create an account."
  - This is accomplished by adding a form where the user can input there details and submit into the database (MongoDB). [register page form](readme_img/register-img.PNG) [Logged in](readme_img/user-loggedin.PNG)
- "As a user who has created an account I want to be able to login."
  - This is completed where a user can input there details previously used to sign up, which is then checked in the database (MongoDB) and is then logged in. [Log In Page](readme_img/log-in-page.PNG) [Logged In](readme_img/user-loggedin.PNG)
- "As a user I want to be able to write a review for a recipe."
  - This was achieved using CRUD (Create) where a user added there review and it was then submited into the database (MongoDB). [Add review button one](readme_img/add-review-button-one.PNG) [Add review button two](readme_img/add-review-button-two.PNG) [add review form](readme_img/add-review-form.PNG) [add review shown in website one](readme_img/review-shown-one.PNG) [add review shown in website two](readme_img/review-shown-one.PNG)
- "As a user I want to be able to delete my review."
  - This was done by using CRUD (Delete) which as user can delete there review only if it is theres. [review delete button one](readme_img/review-delete.PNG)

<span id="owner-stories"></span>

#### Owner Stories
- "I want my users to be able to add there own recipes". 
  - [Add recipe form](readme_img/recipe-form.PNG) [Recipe shown on website](readme_img/recipe-site.PNG)
- "I want my users to be able to find/view other users recipes".
  - [View recipe button](readme_img/view-recipe-button.PNG) [View recipe page](readme_img/view-recipe-page.PNG)
- "I want my users to be able to sign up, sign in and logout". 
  - [register page form](readme_img/register-img.PNG) [Log In Page](readme_img/log-in-page.PNG) [Log Out Button]()
- "I want my users to be able to review other user recipes".
  -  [Add review button one](readme_img/add-review-button-one.PNG) [Add review button two](readme_img/add-review-button-two.PNG) [add review form](readme_img/add-review-form.PNG) [add review shown in website one](readme_img/review-shown-one.PNG) [add review shown in website two](readme_img/review-shown-one.PNG)
- "I want my users to be able to search for recipes".
  - [search bar](readme_img/search-bar.PNG) [Search bar returned results](readme_img/search-bar-results.PNG)
<span id="ux"></span>

## UX

<span id="project-goals"></span>

### Project Goals
* For users to upload there recipes onto the website.
* Users to review other users recipes.
* Profile page where users can see there uploaded recipes.
* Log In/ Log out functionality.
* Ease of use.
* Users can make full use of CRUD functionality for the recipes.

<span id="design"></span>

### Scope
* Allow users to register an account on the website.
* Allow registered users to Create, Read, Update and Delete (CRUD) recipes.
* Create functionality for users to Create, Delete reviews on recipes.
* Create using my current skills, HTML, CSS, JavaScript, Python, Flask and MongoDB

### Structure
* Navigation bar located at the top of the website for ease of navigation through site.
* Logged in users to be able to use CRUD functionality with recipes.

### Surface

#### Colours
I have chosen these set of colours for my website:
* #ffcb9a A beige colour used for the main title on the navbar and important messages for example when a recipe is added
* #116466 A dark green used throughout as the main theme colour, I found this colour easy on the eye and flowed well with the rest of the styles.
* #d1e8e2 A light blue, used for the profile page as it gives good contrast between the recipe cards and username titles.
* white White was used for alot of text with backgrounds as I found it poped well against multicolour backgrounds. 
* black Black was used in key places when against a white background to make text stand out.

#### Icons
In the project, icons were obtained from [Font Awesome](https://fontawesome.com/). Icons were used it two different settings, one way was functional such as social media. The others were for lists in the recipes such as ingredients and steps.

#### Typography
* "Lexend Mega" Used for main pecies of content like titles and headings.
* "Lato" Used for most of the text throughout the website, as it is a clean font and makes it very user-friendly and easy to read.

#### Imagery
When choosing imagery I used [Pexels](https://www.pexels.com/). Images were used mainly for background images in the site as well as a fallback image if user's uploaded image is not avaliable.

#### Defensive Design
- Register Form:
  - The register form has validation that limits the amount of characters for a username and password, the password must contain at least one number and one uppercase and lowercase letter.
- Add and Edit Recipe Form:
  - Recipe name is limited from 2-44 characters and must start with a letter and contain no special characters.
  - 'How many people does this recipe serve?', only accepts number inputs with a maximum of 100, and positive numbers only.
  - The description must be between 10-150 characters.
  - Image URL will only accept URL's ending with jpeg, jpg, gif and png.
  - Preparation and cooking time will only accept positive numbers to a maximum of 1000.
  - All fields are required.
- Add Review Form:
  - Description must be between 10-49 characters.
  - All fields are required.
- A recipe and review can not be deleted with one click, it will open a modal with a yes or no option.

<span id="ia"></span>

#### Information Architecture
The project has four collections in MongoDB, the layout implemented is:
![Database Layout](readme_img/database_layout)

<span id="wireframes"></span>

#### Wireframes
Wireframes are created with [balsamiq](https://balsamiq.com/)
[Wireframes](static/wireframes/recipesWireframes.pdf)

<span id="features"></span>

## Features

<span id="e-features"></span>

### Existing Features
* Created with HTML5, CSS3, Javascript, jQuery, Materialize and MongoDB.
* Home/Index page to give the users an idea of the website with the use of imagery and text, with a call to action button to discover recipes.
* Responsive design.
* Footer with social media links.
* 'Add Recipe' page for users to create there own recipe and add it to the website.
* Reviews button which opens a form, for users to review recipes.
* Search bar for users to search the website for specific recipes.
* Profile page showing when the user signed up and the recipes they have added.

<span id="f-features"></span>

### Features Left To Implement
* A future feature that would be a good addition would be a favrioute button on recipes. This button would save the recipe in the users profile for ease of use to come back to later.
* A future feature I would like to implement would be for more functionality for users to edit there usernames or even delete there account.

<span id="technologies used"></span>

## Technologies Used

**Languages Used:**
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - HTML5 provides the structure for my content.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - CSS3 is used for styling HTML5.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - Used to create functionality.
- [jQuery](https://jquery.com/)
  - Used to create functionality.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  - Python is used for the backend.

**Frameworks, libarys and Other**
- [Google Fonts](https://fonts.google.com/)
  - Used to provide 'Lexend Mega' and 'Lato' fonts for the project.
- [Materialize](https://materializecss.com/)
  - Materialized is used for the design framework
- [FontAwesome](https://fontawesome.com/)
  - FontAwesome is used for icons in the websit such as social links.
- [MongoDB](https://www.mongodb.com/)
  - MongoDB is used as the database for the project.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - Flask is the web framework used to provide libraries, tools and technologies for the app.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
  - Jinja is used for templating Python.
- [https://werkzeug.palletsprojects.com/en/1.0.x/](https://jinja.palletsprojects.com/en/2.11.x/)
  - Werkzeug is used for password hashing and authentication and autohorization.
- [Git](https://git-scm.com/)
  - Git was used for version control.
- [GitHub](https://github.com/)
  - GitHub is used to host the project.
- [Heroku](https://dashboard.heroku.com/)
  - Heroku is used as the cloud plateform to deploy the app.
- [Balsamiq](https://balsamiq.com/)
  - Balsamiq is used for creating wireframes
- [Gitpod](https://www.gitpod.io/)
  - Gitpod was used to devlop the project.

**Testing Tools/ Code validity**
- [Chrome dev tools](https://developer.chrome.com/docs/devtools/open/)
  - Used to check responsiveness and find problems/ bugs.
- [Autoprefixer](https://autoprefixer.github.io/)
  - Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules.
- [W3C Markup Validation](https://validator.w3.org/)
  - The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)
  - The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
- [JShint](https://jshint.com/)
  - JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code.
- [PEP8](http://pep8online.com/)
  - The PEP8 validator is used to check whether there were any errors in the Python code.
- [Pyton Tester](https://extendsclass.com/python-tester.html) 
  - Python code syntax checker
- [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) 
  - Validates all tags are opening and closing correctly.

<span id="testing"></span>

## Testing
The full testing process can be found [here](static/testing/TESTING.md)

<span id="deployment"></span>

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

<span id="resources"></span>

## Resources 
* Code Institute Course Content
* Youtube
* W3C
* Balsamiq
* Stack Overflow
* Code Institute Slack community

<span id="credits"></span>

## Credits 
* [Recipes](https://www.bbc.co.uk/food/recipes)
* [Documentation for assist with creating to top button](https://paulund.co.uk/how-to-create-an-animated-scroll-to-top-button-with-jquery)
* [Pattern Attribute W3Schools](https://www.w3schools.com/tags/att_input_pattern.asp)

### Media

* [Pexels](https://www.pexels.com/) was used for imagery.

<span id="acknowledgments"></span>

### Acknowledgements 
* Mentor Can Sucullu for his feedback and advice throughout, Mentor Precious Ijege for his support and knowledge.
* Tutor support at Code Institute for their assistance.
* Slack community for assistance and questions.

<span id="support"></span>

### Support
For any queries or support contact jack200034@hotmail.com

<a href="#recipes">Back to top</a>