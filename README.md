

## project tips
### testing
to run a  report:
- coverage run --source=app-name manage.py test
- coverage report
to create an interactive html repot: 
- coverage html
- python3 -m http.server

# other
shift + F5      hard page refresh

my-auto     centers an element virtically

https://logomakr.com/
## navbar

#  nutrition tab for subscribers of premium server
#   workout tab for subscribers of basic service
members get 10% discount on all products in store




# Black Panther Fitness

The goal of this website is to provide a place where people come to purchase various health and fitness related products and services. It's a place where they can find all gym and sports related good and 
as well as workout classes and instructors to aid in there pursuit of a healthier lifestyle. 

 
## UX

### User Stories

- As a site user i want to be able to:
    - find an instructor that will help me to reach my fitnes goal.
    - find class that will enable me to reach my fitness goal
    - reach my fitness goal while having fun
    - want to find products that cater to my fitness needs
    - navigate through a site easily
    - access info for my fitness needs
    - find various workout that might appeal to me
    - make friends though classes and find a gym buddy
    - purchase what I need easily with


- As a site owner i want to be able to:
    - create a site that is a one stop shop for everything fitness related.
    - generate some income from the the sale of services and goods
    - build a community of user based around, the sale of workout plans, nutritions and personal trainers services

## Design Choices

### Colours

- **Navbar, Footer and Buttons** - I decided to use ``#e28108fa``(orange) as i was drinking orange juice at the tiem an noticed it's easy on the eyes giving a light refreshing look to the site. It stands out well against the various background images used throughout the site. The site body was left white to accent this colour.


- **Font Colour** - I decided to use ``#000`` (black) for the text within the navbar and footer as it compliments the lighter orange color and made information easy to read.

- **Page Header** - I decided to use ``##212529``(Dark Grey Tint) overlay over the page header image to bring to the forefront the text which i made ``#e0d3c4fa`` (light orange). this allowed for text to not interfere with the background image and make it easier to read.

### Fonts

- [**Concert One**](https://fonts.google.com/specimen/Concert+One?sidebar.open=true&selection.family=Concert+One) - I used this font thoughout the site as I felt that it complemented the colours used on this site and added to the feeling of something refreshing and easy on the eyes (like orange juce).



### Wireframes

- The wireframes for the initial layout of the website were made using [Microsoft Whiteboard](https://www.microsoft.com/en-gb/microsoft-365/microsoft-whiteboard/digital-whiteboard-app) and you can view the wireframes for this site [here]().

- The design layout includes Desktop and Mobile - portrait and landscape views


#### Variation Between Wireframes and Final Product

During the styling phase of the website I stuck to the original wireframe design however; after viewing it live I felt that it brought down the overall design level of the website. It is with this in mind, I did not use the following:

 

## Features
### Existing Features
#### Landing Page
 - The landing page was design to not overwhelm the user when the first visit the site. it has a large backgound image with a page title and a button for users to sign up. The button disappears when the user is logged in.
 - below the backgound image are 3 large responsive links acting like a stylish navigation. When clicked show take the user to the 3 main parts of the site.
#### Navigation bar
#### Cart Page
#### Checkout Page
#### Add Workout Class Page


#### Additional features to be implemented in the future:
- Add a feature within me/my profile navigation link to allow for users to input there biometrics and have it saved in the database to allow for users to track there progress over time. similar to the way the users name and address are store for ease of purchase and delivery.
- a page for users to be able to find and purchase workout routines and nutrition plans.
- A fitness package page that offers a combination of workout classes based on a theme like preperation for the [Ironman](https://www.ironman.com/) competition or white collar boxing.
    - the fitness packages will also discounted based on a set quantity of seesions pre-packaged.
- 

### Features Left to Implement
- fix adding non square images to the datsbase as to not brake the layout of the site
- add a hoverable bootstrap tooltips to difficulty level shown on the workout class detail page. it will show little description for beginner, intermediate and advanced.
- add an about us page and a footer.
- style the landing page.
- fix the quantity buttons border on all relevent pages to match the theme of the site.
- include the relevent text information where needed.
- in the classes opening categories page move the text from the html to the database through adding a description field to the modal.
- add a page showing the gym location.
- update the workout class detail page to show class availability (days and time) by creating additional modals.
- fix the time field on the workout class modal
- style the navbar dropdowns and the nav fonts
- style the instructor page to match the design layout of the workout class pages
- add the instructor detail page

## Technologies Used

- [HTML](https://html.com)

- CSS

- [Font Awesome](https://fontawesome.com/)

- [Javascript](https://www.javascript.com)

- [JQuery](https://jquery.com) - javascript library

- [Python](https://www.python.org/) - Programming language

- [Django](https://www.djangoproject.com/) - web application framework

- [Stripe](https://stripe.com/gb) - Online payment processing

- [Bootstrap](https://getbootstrap.com/) - The project uses **Bootstrap**, a front-end framework to to help build a responsive, mobile-first website.

- [Heroku](https://dashboard.heroku.com) - Deployment

- [Amazon Web Service](https://aws.amazon.com/) - Object data storage, media and static files


## Testing

to run a  report type in the CLI:
- coverage run --source=app-name manage.py test
- coverage report
    - to create an interactive html repot: 
- coverage html
- python3 -m http.server

## Deployment


## Credits

### Content
- Some of the text for the workout class page was taken from [Puregym](https://www.puregym.com/) website

### Media
- The photos used in this site were obtained from :
    - codeinstitute's boutique-ado project
    - [unsplash.com](https://unsplash.com/)

### Acknowledgements

- I received inspiration for this project from:

- [bodybuilding website](https://www.bodybuilding.com) in particular the layout of the search navigation bar 

- [Codecademy](https://www.codecademy.com/) with there various learning material and example code and the colour scheme

- [Gymbox](https://www.gymbox.com/) with the layout of there classes category page

- [Puregym](https://www.puregym.com) with some of the written material and there page layout

During the process of creating this site, I used the following resources to achieve to develop my knowledge and understanding of coding best parctices:


- [Code Institute](https://codeinstitute.net/) - who have provided the resources and learning material

- [Stackoverflow](https://stackoverflow.com/) - very useful for troubleshooting any problems you may have

- [CSS-Tricks](https://css-tricks.com/) - a useful tool for css styling.

- [w3schools](https://www.w3schools.com/) - a very useful resourse to learn from

- [dbdiagram](https://dbdiagram.io) - helps with developing relational databases
