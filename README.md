# Healthier alimentation products finder
This application aims to help the user finds substitutes for all food related products. Based on a selection of product, this application will offer alternatives with a better nutrition grade (nutriscore in French). The user can then decide to save this alternative (or not) and review the saved alternatives.
##

### *Requirements:* 
Please refer to the requirement.txt file and the followinf section of this readme: MySQL installation.
### *MySQL installation:* 
This application uses mySQL, in order to install it please visit: 
https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/
### *Database connection parameters:*
Regarding the connection to mySQL, please create a file named sqlCredentials.py inside the classes/parameters folder.
You can then copy/paste the code inside exple-sqlCredentials.txt in your brand new sqlCredentials.py file and **update it with your specific host, user and password**.
### *Parameters:* 
You can change the number of categories and product per category you want inside the classes/parameters/constants.py file
### *The open food fact initiative:* 
For more information please refer to: https://fr.openfoodfacts.org/
This application uses the open food fact API. 
Open Food Facts is a non-profit project developed by thousands of volunteers from around the world.
As the data comes from volunteers, it might be incomplete and even sometimes not accurate, please use the information from this application with caution.

<!-- Application scope:
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
The application save (or not) the substitute inside a dedicated table of our database. -->




