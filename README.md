Application scope:
Search for aliments in the OFF database (we will use the acronym OFF in this file to refer to Open Food Facts).
Create a local database and store a defined number of aliments from a defined number of categories.(both those numbers being declared in the CONSTANT.py file).


User possibilities:
/- 1 Flush the database (used primarily for development purposes).
/- 2 Find a substitute to an aliment
/- 3 Display the substitutes to aliments that have been saved
/- 4 Quit the program 

Detailed scenario for "-/ 2 Find a substitute to an aliment"
The application display the list of categories with an id for each category.
The user chooses a category by selecting the associated id.
The application displays the products from this category
The user can choose a product from this category for which he desires a substitute.
The program then displays one of several potential subsitutes with a better nutriscore.
The user chooses one of the substitues.
The application offers to save this substitute.
The user chooses to save (or not).
The application save (or not) the substitute inside a dedicated table of our database.




