# Exercise 1.2
## Task
- **name (str):** Contains the name of the recipe
- **cooking_time (int):** Contains the cooking time in minutes
- **ingredients (list):** Contains a number of ingredients, each of the str data type

I have chosen to employ dictionaries as a means of storing the aforementioned data for each recipe, primarily due to the diverse data types that require storage and the versatility inherent in dictionaries. Dictionaries can accommodate recipe names as strings, ingredients as lists, and cooking times as integers. Additionally, their mutability enables us to modify or expand upon individual recipe entries in the future.

**all_recipes = [ ]**

I have opted to utilize a list as the overarching data structure for housing the recipe dictionaries. This choice is predicated on the sequential nature of lists, which makes them ideal for the storage of multiple recipes. Furthermore, their malleability allows for easy modifications, should such alterations become necessary.