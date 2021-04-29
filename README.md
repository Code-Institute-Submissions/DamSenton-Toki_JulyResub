# Walkies!

## Milestone Project 3

![ Responive Design](media/responsive.JPG)

## Introduction

For my fourth milestone project I wanted to make sure to nail all of the requirements, so I set out to really understand Django and Python and how to bring them together to make an incredibly functional and responsive website.

This project posed my biggest hurdle yet, as I can admit I am not the best with backend development. So after deciding to really push myself, I set to use all of the knowledge I had gained from the mini project, and adapt this into something I could call my own.

This project also would help me with any future endeavors, as my wife has already asked for a website, and this pushed me even further.

*Tōki* is a fictional ceramics company which aims to bring world class art to everyone.

I wanted a section for articles to give users a way to explore the world of ceramics with easy to digest articles from "professionals".

The idea for Tōki was my own after recently watching, and admittedly getting very involved in, a pottery show on T.V and realising how much I like the art form.


[Live view of my project](https://toki-damsenton.herokuapp.com)


<hr>

## **User Experience**

### Project aims

This project needed to be a fully functional e-commerce website using the Django framework and Python code.

The project needed a fully-functional payment system, which was achieved using Stripe.

Another challenge was image and static file hosting, but this was solved using the Amazon AWS S3 buckets, this service hosts the files remotely, and Heroku can use this to use the code for the website.

With the above in mind, I wanted to make the e-commerce website, but also make it so the page can be personal too, with reviews and articles to help keep up user engagement, and ensure that people want to keep coming back to the website.


<hr>

## User stories

### Stakeholders
- The main Stakeholdersfor this website would be heavily interested in revenue generation, as this is an e-commerce website, the main goal for the company is revenue, and thanks to the bag and checkout app while also using Stripe, this was achieved.

- Stakeholders would also want to keep up user retention, to ensure traffic is high, and sales are consistent.

- The ability to review products would be great so that storeowners can see which products are more popular so they can stock more, or discontinue them.


### New users
- New users would like to find an easily navigatable webage with a consistent colour scheme and intuitive design.

- A new user would also liek the optin to make an account if they like the website enough.

 - Another key feature for a new user, who may not want to be signed up, woudl be the ability to buy products without having an account.

### Returning users
- Returning users would want a way to see their information in their account, and edit this according to their own preferences, and possible changes of name/address etc.

- Returning users usually means repat customers, so a way to see their order history would be very beneficial.

- These users would also benefit from regular updates to the articles section so they can keep up to date with the company and the products.

### Mobile and tablet users

- Mobile users would need a responsive website that works well on smaller screens without word-wrapping, quality loss or image distortion.


<hr>

## Design Planes as defined by [Lauviaxh](http://donatalesiak.panel.uwe.ac.uk/wordpress/2018/10/30/the-five-planes-the-elements-of-user-experience/)

- Strategy Plane: Tōki would need to be a functional e-commerce website that appeals to a niche by using customer engagement and feedback in order to drive sales. It would also need to be able to store data for the customer should they want to create an account.

- Scope Plane: This project woudl need a robust framework in order to combine all the apps fluidly, so using Django was the most viable choice. <br>
Tōki needs navigation, a home view for new users, a way for users to view, add, purchase and review products. The use of an article section for customer engagement would also be useful.

- Structure Plane: After the above was decided, The structre of the webpage was decided, and the website was conceptualised. I knnew i wanted earthy tones for the colour scheme to match the pottery theme, and how the navigation bar would work, making use of dropdowns for a cleaner screen. <br>Use of Bootstraps grid system woul also be invaluable as this provides 'out-of-the-box' responsiveness which is vital for mobile-first development. <br> The structure plane also takes into account the database structure, and for this I used SQLite for development environents, and Heroku's Postgress and Amazon's AWS for deployed code.<br>
I wanted to break the data up into more readble chunks, so using JSON really helped with this. Having the product data split into individual products, their corresponding categories, and the reviews for each product made for much more readble code.

- Skeleton Plane: With all of the above mentioned, the way a use rwould experience this website was vital, I wanted to make the experience as seamless as possible, with a permamnet navbar that stays on the screen when scrolled made sure that a user is never just stuck on a page.<br>
Subtle hints from the carousel images and also the icon in the navbar encourage users to create an account, and from here, you are instantly made aware of the other features that come with this, such as delivery information and order history.<br>
Toasts would also prove very useful as they give instant feedback to a customer with certain inputs such as adding a product to the bag, or trying to access a page they aren't permitted to.

- Surface Plane: With all of the above mapped out, I set to work on creating the surface of the webpage. Starting with [Figma](https://www.figma.com/file/F24anz4HjMIsBDzgAt1gcy/Tōki)<br>
Settling on the way I would present content was a big concern, 

<hr>

## Wireframes

- Desktop wireframe
![Desktop Design](media/figma-desktop.JPG)

- Mobile wireframe
![Mobile Design](media/figma-mobile.JPG)

- Tablet wireframe
![Tablet Design](media/figma-tablet.JPG)

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

[Django](https://en.wikipedia.org/wiki/Django_(web_framework))
- Django sometimes stylized as django is a Python-based free and open-source web framework that follows the model-template-views architectural pattern. It is maintained by the Django Software Foundation (DSF), an American independent organization established as a 501(c)(3) non-profit.

[Heroku](https://en.wikipedia.org/wiki/Heroku)
- Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.

[Stripe](https://en.wikipedia.org/wiki/Stripe_(company))
- Stripe is an Irish-American financial services and software as a service (SaaS) company dual-headquartered in San Francisco, California and Dublin, Ireland. The company primarily offers payment processing software and application programming interfaces (APIs) for e-commerce websites and mobile applications.

[Font Awesome](https://fontawesome.com/)

- Font Awesome is a tool used to provide icons which add to the overall aesthetic of the web page.

[Google Fonts](https://fonts.google.com/)

- Google Fonts provides the user with different options for fonts to be used in web pages, further adding to the personalization of each page.


<hr>

## Features and apps

### Home app
The home app would serve as the main landing page for the web page, with no models, and a simple view, the only fucntion for this app is to load the user into the first page.

This being said, once this is launched, the the base template is extended and this brings the navbar, and, the bag app and the profile app to the user.

### Products app
The product app focuses on storing data about products, and manipulating this data to display to the user.

The models for this app would be based on product informtion such as product name, details and price etc.
<br>
This app also allows admins of the website to create new product listings, and edit existing ones to reflect market demand.
<br>
When a user clicks on a product, they are taken to the product details page, here a user is able to add the product to their bag, and also make use of a quantity selctory to add multiple of each product to their bag.
<br>
Within the product details page, users who are logged in with an authenticated account can leave a review of a product. Thes ereviews are displayed to all users regardless of whether they have an account or not.


### Bag App
The bag app allows users to add products from the product app into their bag, this app also provides the user with what is in their bag how much their current bag costs.
<br>
Users are also shown how much more they need to spend in order to recieve free delivery, if this threshold is not met, then the bag app calculates 10% of the total of the contents and adds this on as a delivery charge.
<br>
Within the bag app, users are able to amend the contents, by either removing the product, or increasing the amount of them.


### Checkout App
The checkout app is integral to this project, as the whole point of it is the be a fully functional e-commerce website.
<br>
Users who purchase products also have the option to save their delivery details to their profile to make the next purchase that little bit mroe hassle-free.
<br>
The checkout app makes use of Stripe to handle payments, users wanting to make a purchase, can test this by using the following details;<br>
- Card Number: 4242 4242 4242 4242
- Postcode: 42424
- CVC 424
- Expiration: 04/24

<br>
Upon a successful puchase, users are given feedback in the form of a loading psinner, indicating that their payemtn is being processed.


### Profiles App
This app handles user data, and works hand in hand with the checkout app to bring a seamless experince for users who want to have a quicker checkout experience.
<br>
Users can update their information should they wish to.
<br>
Logged in users who have made purchases are shown their order history, that when clicked on, brings them to an overview of their previous purchses. 

### Articles App
The articles app makes use of a similar structure to the products app, making use of JSON files to store the articles and making use of the edit/add forms that the products app uses.
<br>
This app allows users to read regularly updated articles to keep up witht he industry.
<br>
Similar to the products app, this app gives admins the ability to create, edit and delete articles.

### Allauth
Allauth is a feature of Django that handles a wide range of user-related templates, such as the login/logout forms and also the password reset functionality.

### Emails
Upon successful account registration, users are sent an email to authenticate their account.
<br>
When users succesfully purchase a product, they are also sent an email with details of their purchase.

## Desired Features
With more time, I would have liked to have implemted an app for users to book onto pottery courses, making use of Google Maps API to show their nearest studio.
<br>
I also saw a lot of other student susing a loyalty scheme, this would also be a very desired feature for me, but with limited time, and a lack of knowledge, I was unable to complete this.
<hr>

## Testing
Most of my testing was done through the use of Chrome Dev Tools to test the responsiveness of the website on smaller screens, making changes in Dev Tools allows real time alterations that you can copy over into your code.

Django comes with it's own debugger which when triggered, provides the developer with detailed error messages which make testing a lot easier. A common problem I ran into was proper use of views and models to present different pages, but with proper understanding of these error messages they were easily fixed.

All of the links for the website were manually tested by myself, these all work as intended. One problem I ran into was styling the allauth buttons, as they have set stylings, but using dev tools, I was able to figure out how to style these to fit my site.

The bag app is limited to 99 of each product, to preserve website integrity. Users are also unable to add 0 of a product to the bag as this would provide an unresponsive error from the bag app, this is also the same for the chekout app, users are unable to add excess or underflow items here.






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


