class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name 
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f'{item} added to your shopping list')
        else:
            print(f'{item} is already on your shopping list')

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f'{item} removed from your shopping list')
        else: 
            print(f'{item} is not on your shopping list')   

    def view_list(self):
        print(self.list_name)
        print('-----------------------------------------------------------')
        for item in self.shopping_list:
            print('-' + str(item))
    
    def merge_lists(self, obj):
        merged_lists_name = 'Merged List - ' + str(self.list_name) + ' + ' + str(obj.list_name)
        merged_lists_obj = ShoppingList(merged_lists_name)
        
        # Merge items from the current list
        merged_lists_obj.shopping_list = self.shopping_list.copy()
        
        # Add the items from the other list without duplicates
        for item in obj.shopping_list:
            if item not in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)
        
        return merged_lists_obj

pet_store_list = ShoppingList("Pet Store Shopping List")

for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)

# Removing "flea collar" from the shopping list
pet_store_list.remove_item("flea collars")

# Try to add "frisbee" again
pet_store_list.add_item("frisbee")

pet_store_list.view_list()



