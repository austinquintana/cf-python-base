import pickle

def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'hard'
    return difficulty

def take_recipe():
    name = input("Enter recipe name: ")
    cooking_time_str = input("Enter cooking time in minutes: ")
    
    # Attempt to extract the integer part from the input string
    try:
        cooking_time = int(cooking_time_str.split()[0])
    except ValueError:
        print("Invalid input for cooking time. Please enter a valid number of minutes.")
        return take_recipe()  # Recursively ask for input again
    
    ingredients = []
    n = int(input("Enter number of ingredients: "))
    for ingredient in range(n):
        ingredient = input("Enter ingredient: ")
        ingredients.append(ingredient)
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    recipe['difficulty'] = calc_difficulty(recipe)
    return recipe

recipes_list = []
all_ingredients = []

filename = input('Enter the filename where your recipes are stored: ')

try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print('File not found. Creating a new file.')
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print('Unexpected error occurred. Creating a new file.')
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

num = int(input("How many recipes would you like to enter?: "))
for i in range(num):
    recipe = take_recipe()
    print(recipe)
    recipes_list.append(recipe)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

new_file_name = input('Enter a name for your new file: ')
with open(new_file_name, 'wb') as file:
    pickle.dump(data, file)
