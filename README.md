# Recipe app- web apps final project

Made by:
- ANGELA DURÁN 100472766
- DANIEL KWAPIEN 100472421
- AFINA NUROVA 100472901

Extras:

- Search view with ingredient search filter: the search bar allows to search by description or title and the ingredient search allows
to search recipes with contain all the selected ingredients. The ingredient filter is applied in the main.new_search and main.new_search_ingredient
using a method created inside the Recipe class.

- Recipe photos: a user can upload photos when creating a recipe. These are displayed at the top of the recipe view with a carrusel effect.
They can also be seen from the main view, where the recipes are shown.

- Recipe creation form using WTF Forms library: these are created in the forms.py file and used in the recipe_creation.html
inside the templates/recipe_creation template.

- Recipe creation form using javascript and ajax: In recipe_creation.html, 95 til end. Used for adding new entries in the form when the user
pleases.

- Drink recommendations: we created a new model class called Drink which is related with the Recipe class; this allows us to post recommendations 
of drinks when creating the recipe. It is not mandatory for the user to give a drink recommendation. 
The recipe view only shows the Drinks section when there are recommendations (similarly to the Photos section, which would appear when other users
different than the creator have posted photos to a recipe)

- PDF download of the recipes: we used the xhtml2pdf and reportlab libraries to offer the possibility of downloading a recipe as a pdf from the
recipe view. This button is in the recipe.html file, line 146. The action of this button is in main.download_pdf, which calls another function.
A special html and css style are used for the pdf version of the recipe, and these are in the recipe_pdf.html file.

- User view using javascript: interactive view where the user can click on the bar options and see displayed the Posts, Photos and Ratings. If a user is looking at their own profile there is also a tab called Bookmarks. 

- Star representation for the recipe ratings: we created a method in the model class Recipe using sqlalchemy.

Some notes:
- View may vary depending on some factors: if you are logged in or not, if the recipe has photos or not, if users have uploaded photos to a recipe or not, if drinks have been recommended for some recipe...

