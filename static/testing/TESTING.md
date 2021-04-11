# Testing 
<span id="testing"></span>

## Table of Contents 
> - [User/Owner Stories Testing](#uo-stories)
> - [Code Validation](#validation)
>   - [HTML](#html)
>   - [CSS](#css)
>   - [JavaScript](#js)
>   - [Python](#py)
> - [CRUD/Function Testing](#crud)
>   - [Add Recipe (Create)](#add-recipe)
>   - [Add Review (Create)](#add-review)
>   - [Edit Recipe (Update)](#edit-recipe)
>   - [Search Recipe (Read)](#search-recipe)
>   - [Delete Recipe (Delete)](#delete-recipe)
>   - [Delete Review (Delete)](#delete-review)
>   - [Profile](#profile)
>   - [Login](#login)
>   - [Register](#register)
>   - [View Recipe](#view)
>   - [Recipe Page](#recipe)
>   - [Index](#index)
>   - [error](#error)
> - [Manual Testing](#manual)
> - [Responsive Testing](#responsive)

<span id="uo-stories"></span>

## User/Owner Story Testing **Also demonstrated in [Readme](../../README.md)**
- "As a user I want to be able to delete my recipe."
  - **Testing:** From the logged in account I went to 'profle' and clicked 'delete' on a recipe, which opened the 'are you sure you want to delete' modal, I clicked delete again which deleted the recipe fully from the website/ database.
- "As a user I want to be able to easily view other users recipes."
  - **Testing:** On the recipe page I clicked on a recipe card's view button, which opened the view page, this worked correctly.
- "As a user I want to be able to use a search bar to find recipes."
  - Using the search bar on the recipes page, I added my query by searching for a recipe name, this returned the correct results.
- "As a user I want to be able to create an account."
  - I went to the 'register' page, using the form provided I added my details and clicked sign up, this then took me to my profile page which is correct. I also checked the database to check the user was added and it was added correctly.
- "As a user who has created an account I want to be able to login."
  - Making sure I was logged out, I clicked 'Log In', using the details I signed up with I added them to the form and clicked login, this took me to my profile page whhich is correct.
- "As a user I want to be able to write a review for a recipe."
  - On the recipes page I went to a random recipe and clicked 'reviews' from there I clicked 'add review' and added my review using the form and then clicked submit. I went to the same review and clicked 'reviews' and the review added was there, I also checked the database to find it was correctly added there. I also repeated the same but using the view page.
- "As a user I want to be able to delete my review."
  - Going to a review that I added, I clicked on 'delete' which deleted my review from the site after refreshing. I went to my database and checked it was deleted there, this was deleted correctly.

##### Owner stories link with user stories so they have been tested.

<span id="validation"></span>

### Code Validation

<span id="html"></span>

#### HTML 
Passed [W3C Code Validator](https://validator.w3.org/)

<span id="css"></span>

#### CSS
Passed [W3C Code Validator]()
- **1 error** - 97 .index-h1 Value Error : text-shadow Too many values or values are not recognized : 2px 2px 2px 2px rgb(0, 0, 0, 0.5) **Fixed**

<span id="js"></span>

#### JavaScript
Passed [JSHint]()
- Two warnings - Missing semicolons on line number 68 and 88 **Corrected**

<span id="py"></span>

#### Python 
Autopepe8 installed as a dependency for checking code as written, all python ran through [ExtendsClass Python Syntax Checker]()

<span id="crud"></span>

### CRUD/function Testing
#### Add Recipe Function (Create)
- Step by step test
  - Clicked on 'new recipe' in the navbar
  - Tested all field validation to check when the wrong type of data was added it would not submit.
  - Added correct data to the fields clicked submit.
  - Checked a flash image was shown when a recipe was added.
  - Checked MongoDB to see if recipe had been added.
  - Checked recipe page and profile page to check the recipe was displaying correctly on the site.
* Checked endpoints using the url that a logged out user cannot add recipes and will be redirected.

<span id="add-recipe"></span>

#### Add Review Function (Create)
- Step by step test
  - Clicked on a recipe, scrolled to the bottom of the page and clicked add review.
  - Checked all field validation worked as wanted, and the review would not submit without correct validation.
  - On the add review form I added data in to the fields and clicked submit.
  - Checked a flash image was shown when a review was added.
  - Checked MongoDB to check review was added, checked website to check the review was displaying on the recipe.
* Checked endpoints using the url that a logged out user could not add a review and would be redirected to login.
* Added a recipe and checked I could not add a review on it (To make sure owner of the recipes cannot add reviews).

<span id="edit-recipe"></span>

#### Edit Recipe Function (Update)
- Step by step test
  - Clicked on profile and clicked edit on a recipe.
  - Checked field validation worked and was the same as add recipe.
  - Scrolled to the bottom and clicked cancel to check no changes were made to the recipe.
  - Changed all fields in to new data and clicked edit at the bottom.
  - Checked a flash message was shown when a recipe was edited.
  - Checked MongoDB to make sure the information was updated.
  - Checked the recipe on the website to make sure the correct new information was displaying.
* Checked endpoints using the url that only the user who added the recipe could edit it (tested with logged out user/other user accounts).

<span id="search-recipe"></span>

#### Search Function (READ)
* Clicked submit button with no entries in any fields - Validation worked showing box with the text 'please fill in this field'.
* Entered valid keyword and page returns relevant resource(s) containing that keyword.
* Entered invalid keyword and page returns the message: 'No results found'.
* Clicked Reset button and this clears the search inputs to default and goes back to show all recipes.

<span id="delete-recipe"></span>

#### Delete Recipe Function (Delete)
- Step by step test
  - Clicked on profile page and clicked delete on a recipe.
  - This opened a modal which showed text 'Are You Sure You Want To Delete This Recipe' with an option yes or no.
  - Clicked no and checked the recipe was not removed.
  - Clicked yes and check the recipe was removed from the database and website.
  - Checked a flash message was shown when a recipe was deleted.
* Checked endpoints using the url, that only the user who added the recipe could delete it.

<span id="delete-review"></span>

#### Delete Review Function (Delete)
- Step by step test
  - Clicked on another users recipe where I added a review.
  - Clicked delete on the review which opened a modal.
  - The modal showed 'Are you sure you want to delete this review?' with options yes or no.
  - I clicked no to check the review was not removed.
  - I clicked yes to check the review was deleted from the database and website.
  - Check flash message showed when a review was deleted.
* Checked endpoints that only the user who added the review could delete it.

<span id="profile"></span>

#### Profile Function 
- Step by step test
  - Created a new user using the register form to check it opened a new profile for the user.
  - Checked profile showed only the added users recipes or if none show a message where add one.
  - Checked registration date matched the time when the user was added to the database.
* Using another user account I checked that other users profiles was not accessible, also tested with a logged out user.

<span id="login"></span>

#### Login Function 
* With a previously registerd account, I added the correct username and password to check it opened to the profile page.
* Using incorrect details I checked that a flash message showed and that I was not logged in.

<span id="register"></span>

#### Register Function 
- Step by step test
  - Making sure I was logged out I clicked 'register' on the navbar.
  - I clicked the 'Log In' link at the bottom of the form to check it took me to my login page.
  - I checked the field validation by adding incorrect data to the form, clicked 'signup' to make sure it did not submit.
  - Added same username as another user to check it did not submit and a flash message was shown.
  - I then added correct data to the form and clicked submit.
  - Checked I was took to the user profile page and that a flash message was shown.
  - Checked database to check the user was added.

<span id="view"></span>

#### View Recipe Function 
- Step by step test
  - Clicked the 'recipes' page on the navbar.
  - Clicked view on a recipe card to check the correct page displayed.

<span id="recipe"></span>

#### Recipe Page Function
- Step by step
  - Clicked the 'recipes' page on the navbar and checked that all recipes show.
  - Check pagination works when more than 8 recipes are added.

<span id="index"></span>

#### Index Page Function
- Step by step
   - Entered the website URL and clicked enter.
  - Checked website opened up on the Index Page.
  - Checked Discover button worked correctly.

#### Navbar/Footer
- Navbar
  - Checked all navbar links opened correct pages.
  - Checked sidenav worked on smaller devices.
  - Checked links in sidenav.
- Footer
  - Checked social links open correct websites.

<span id="error"></span>

#### Error Pages
* All error pages checked.

##### **All Tested with multiple accounts and non registered user**

### Responsive Tests

* Used [Responsive design checker](https://www.responsivedesignchecker.com/)

- DevTools - Devices tested across a range of widths:
  - Mobiles: iphone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

- Viewed on physical devices:
  - Mobiles: small phone (320px) | large phone (414px)
  - Tablets: large tablet (768px)
  - Desktops: Medium laptop (1366px) | Large Desktop screen (1920px) | Very Large Desktop screen (1440px)

- Viewed site on above ranges (including Responsive mode) on various browsers:
  - Google Chrome
  - Firefox
  - Brave
  - Opera
  - Safari

### Known Issues and Bugs
- **Issue with the search pagination** On the recipes and search function the pagnation will create a new page for every 8 recipes, If I then search and return less than 8 recipes the page numbers will stay at the bottom, if I click page 2 this will show the message ['no results'](../../readme_img/no-results.PNG). If a search takes place and returns 9 results the pagination will work fine and the 9th recipe will be shown on the [next page](../../readme_img/next-page.PNG). After speaking with a tutor and time limitations it was a bug that could not be fixed, but with the tutor agreeing that this causes no major issues and pagination does work correctly and results are returned as they should.
  - **Update** Since writing this known issue and added more recipes to the website, the bug seems to of fixed, Because of time limitations I will keep this bug in known issues.
- Warning in app.py for pagination 'page' [Seen here](../../readme_img/page-error.PNG) After testing found this causes no issues on the website, spoke with tutor who said this is okay to note in known issues.

### Deployment
* Ensured deployed page on Heroku loads up correctly.
* Ensured Debug variable in app.py file is set to False.
* Confirmed that there is no difference between the deployed version and the development version.

<a href="#testing">Back to top</a>