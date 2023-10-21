def recipes():
    recipes_list = []
    ingredients_list = []

    def take_recipe():
        name = input("Enter recipe name: ")
        cooking_time = int(input("Enter cooking time (in minutes): "))
        ingredients = []
        n = int(input("Enter number of ingredients: "))
        for i in range(n):
            ingredient = input("Enter ingredient: ")
            ingredients.append(ingredient)
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)

        difficulty = ''  # Initialize the difficulty
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'easy'
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'medium'
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'intermediate'
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'hard'

        recipe = {'name': name, 'cooking_time': cooking_time,
                  'ingredients': ingredients, 'difficulty': difficulty}  # Include the difficulty
        recipes_list.append(recipe)  # Append the recipe to the list
        return recipe

    num = int(input("Enter number of recipes: "))
    for i in range(num):
        recipe = take_recipe()
        print(recipe)

    def print_ingredients():
        ingredients_list.sort()
        print('All Ingredients')
        print('_______________')
        for ingredient in ingredients_list:
            print(ingredient)

    for recipe in recipes_list:
        print('Recipe:', recipe['name'])
        print('Cooking time (min):', recipe['cooking_time'])
        print('Ingredients:')
        for ingredient in recipe['ingredients']:
            print(ingredient)
        print('Difficulty:', recipe['difficulty'])

    print_ingredients()

if __name__ == "__main__":
    recipes()


