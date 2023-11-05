import pickle

with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Tea Recipe - ")
print("Name: " + recipe['Name'])
print("Ingredients: " + str(recipe['Ingredients']))
print("Cooking Time: " + recipe['Cooking Time'])
print("Difficulty: " + recipe['Difficulty'])