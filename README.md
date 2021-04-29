# Walkies!

## Milestone Project 3

![ Responive Design](media/responsive.JPG)

## Introduction





[Live view of my project](https://toki-damsenton.herokuapp.com)

<hr>

## **User Experience**

### Project aims



<hr>

### User stories

### Stakeholders


### New users


### Returning users


### Mobile user


<hr>

## Design Planes

- Strategy Plane: As stated above, I wanted to create a webpage that brought people together with one goal in mind, walking dogs. I also wanted to flex my newly found Python muscles and put my knowledge of MongoDB and Jinja to good use and integrate a system which is easy to use for all types of users.

- Scope Plane: I knew i wanted to give users the ability to sign up to this webpage, but I wanted two types of users, Walkers and Owners. With a new found skill in Jinja, I wanted to use this to have these users connect on the back-end by matching them based on age groups and location so that only certain users are exposed to data relevant to them.

- Structure Plane: Having decided on key features, I set to work on the overall structure of my web page, focussing heavily on mobile first, responsive design which used the incredible grid system and flex-box features which does a lot of heavy lifting with responsive design. 
I decided on a basic structure which uses a multi-page structure to allow for account registration, sign-in, user profiles and CRUD funtionality for owners to allow then to create, read, edit and delete new bespoke walks for theie dog(s).

- Skeleton Plane: As above, I knew i would be using the grid system and flex-box for this project, so the placement for my content was set to center-align to make this seamlessacross all screen sizes. My buttons we placed centrally also to make use of the afformentioned grid system. I wanted first time users to know exaclty how to use the webpage and how to navigate this, so my navbar is what I consider industry standard, and as per an above user story, this seems to have paid off.

- Surface Plane: With all of he above mapped out, I set to work on creating the surface of the webpage. Starting with [Figma](https://www.figma.com/file/fYDp7xJVwoSdtarTEg7e4n/Walkies-Design) I set out the structure I wanted to follow, and also made sure to cement a theme early on, which tied the whole website together.
I decided to use pastel colours as I wanted a playful and friendly website which would appeal to users of all ages. I also decided on a quirky font from Google Fonts and a background from [Harryarts @ www.freepik.com](https://www.freepik.com/vectors/background) which added more personaltiy to the web page.

<hr>

## Wireframes

- Desktop wireframe
![Desktop Design]()

- Mobile wireframe
![Mobile Design]()

- Tablet wireframe
![Tablet Design]()

[Full Wireframe]()
<hr>

## Technologies used

- For this website, I have utilised HTML5, CSS3, JavaScript, Python, Bootstrap, JQuery, Django and Heroku

[HTML5](https://en.wikipedia.org/wiki/HTML5)

- This language is used to build the overall body of the page, from text, to page structures.

[CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)

- CSS3 is used to style the elements on the page. CSS3 is responsible for the colour scheme, and the layout of the page.

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- JavaScript is used to manipulate the logic of the page. I used this extensively for the Drink Matcher page.

[JQuery](https://jquery.com/)

- JQuery is a JavasCript library which allows users to use pre-written code to achieve a JavaScript goal.

[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- Python is an interpreted, high-level and general-purpose programming language. I used this for the brains of the app, making use of app routes and app views to carry out complex functions out of sight of the user.

[Django]()

[Heroku]()

[Font Awesome](https://fontawesome.com/)

- Font Awesome is a tool used to provide icons which add to the overall aesthetic of the web page.

[Google Fonts](https://fonts.google.com/)

- Google Fonts provides the user with different options for fonts to be used in web pages, further adding to the personalization of each page.


<hr>

## Features



## Desired Features

<hr>

## Testing



<hr>

## Code Validation

### HTML Validator (W3C):



 [HTML Code Validation](static/code-validation/html).

### CSS Validator (W3C):


 [CSS Code Validation](static/code-validation/css).

### JavaScript Validator (JSHint)

[JavaScript Errors](static/code-validation/javascript).

### Python Validator (Extendsclass.com)


<hr>

## Responsiveness



### Chrome Developer Tools


<hr>

## Testing Links

<hr>

## Database Schema

<hr>

## Database Entries / Data Retrieval


<hr>

## Project Deployment

My project was created exclusivley in GitPod and using Git Version Control, I was able to periodically commit and push my code to GitHub.

This project is also hosted on Heroku, and using automatic deployments from GitHub, this is a mirror of my original code.

- To start this project, I had to create a GitHub profile, I then created a new repository using the on-screen instructions. When setting up my repository,

- I utilized the Code Institute template which provides basic boiler text.

- Once my code was written, and pushed to GitHub, I opened up my GitHub profile and navigated to the settings in my repository.

- From the settings, I scrolled down to the GitHub Pages section and selected the _Master Branch_ source.

- With these settings confirmed, the page is now live on GitHub Pages, and free to view by all in a web browser.

- In the CLI(Command Line Interface) i Installed Django, and all of my subsequent requirements using pip3 install Django.

- From here I used 'python3 manage.py startapp toki' to create my first app, which installed all of the relevant python files ready for use. This method was also used to install of the apps in the workspace. 

- When my code was halfway done, I connected my workspcae to Heroku.

- I created a Heroku account by first navigating to [Heroku](https://dashboard.heroku.com/apps), and creating an account. From here, I selected create a new app, and this brought me to create an app name and select the region for it's hosting.
From here, I entered in my GitHub details and linked the account.
In the app settings, perhaps ne of the most important parts of this project, I entered in multiple variables into the section labelled 'config vars'. These config vars are hidden from any code pushed to GitHub and Heroku unless you are the owner of the repository. These config vars are essential to the connection between my app and MongoDB, utilizing my 'SECRET_KEY', 'MONGO_URI', 'MONGO_DBNAME', 'PORT' and 'IP' variables set up in my env.py file on GitPod.

- Once my repository was created on GitHub, I was able to link this to my Heroku profile.

- Any users wishing to view this code, or if they would like to use it for inspiration, they can do so on [My GitHub Page](https://github.com/DamSenton/Toki)



<hr>

## Content

All content for this website is fictional, and was written by myself for creative and scholastic purposes.

The images for the website were taken from [Unsplash](https://unsplash.com). All of these images are extremely high quality and free to use.

## Code

The code for this project was heavily inspired by Boutique Ado, as all of the apps are integral to an e-commerce website, and "there is no need to re-invent the wheel" springs to mind, this being said, I took it upon myself to style the website to avoid too many similarities, and to put my own personal spin on things.

Most of the rest of the code for this project was written by myself, however, as stated in code comments in my style.css file, the back-to-top button was provided by [Heather Tovey](https://heathertovey.com/blog/floating-back-to-top-button).

For extra style accross the page, I opted to use a new block divider, this was free to use from [Codepen.Io](https://codepen.io/stg/pen/ZYYQMJ)

I took inspiration from previous projects and used old code such as my nav-bar-hide.js code and my back to top buttons.

<hr>

## Special Thanks


