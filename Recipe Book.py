recipes = []

def add_recipe():
    recipe_name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    instructions = input("Enter cooking instructions: ")
    cooking_time = input("Enter cooking time (minutes): ")
    
    recipe = {
        "name": recipe_name,
        "ingredients": ingredients,
        "instructions": instructions,
        "cooking_time": cooking_time
    }
    
    recipes.append(recipe)
    print("Recipe added successfully!\n")

def view_recipes():
    if not recipes:
        print("No recipes found.\n")
    else:
        print("Recipes:")
        for i, recipe in enumerate(recipes, 1):
            print(f"{i}. {recipe['name']}")
        print()

def view_recipe_details(index):
    recipe = recipes[index]
    print(f"\nRecipe Details for {recipe['name']}:")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Instructions: {recipe['instructions']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes\n")

def main():
    while True:
        print("Recipe Book")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. View Recipe Details")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            view_recipes()
            if recipes:
                recipe_index = int(input("Enter the recipe number to view details: ")) - 1
                if 0 <= recipe_index < len(recipes):
                    view_recipe_details(recipe_index)
                else:
                    print("Invalid recipe number. Please enter a valid number.\n")
            else:
                print("No recipes available. Please add a recipe first.\n")
        elif choice == '4':
            print("Exiting Recipe Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
