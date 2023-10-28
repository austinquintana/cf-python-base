import pickle

def display_recipe(recipe):
    print('Name:', recipe['name'])
    print('Cooking time in minutes:', recipe['cooking_time'])
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty:', recipe['difficulty'])

def search_ingredient(data):
    ingredients_list = data['all_ingredients']
    indexed_ingredients_list = list(enumerate(ingredients_list, 1))

    for ingredient in indexed_ingredients_list:
        print('No.', ingredient[0], ' - ', ingredient[1])

    try:
        chosen_num = int(input('Enter the number of your ingredient: '))
        index = chosen_num - 1
        ingredient_searched = ingredients_list[index].strip().lower()  # Normalize and make it lowercase
    except IndexError:
        print('The number you entered is not valid.')
        return
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return
    except:
        print('An unexpected error occurred.')
        return

    recipes_with_ingredient = []

    for recipe in data['recipes_list']:
        for recipe_ing in recipe['ingredients']:
            if ingredient_searched in recipe_ing.lower():
                recipes_with_ingredient.append(recipe)

    if not recipes_with_ingredient:
        print('No recipes include the searched ingredient.')
    else:
        print('The following recipes include the searched ingredient:')
        print('------------------------------------------------------')
        for recipe in recipes_with_ingredient:
            display_recipe(recipe)

filename = input('Enter the filename where your recipes are stored: ')

try:
    with open(filename, 'rb') as recipes_file:
        data = pickle.load(recipes_file)
except FileNotFoundError:
    print('File not found.')
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print('An unexpected error occurred.')
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    search_ingredient(data)
finally:
    recipes_file.close()


