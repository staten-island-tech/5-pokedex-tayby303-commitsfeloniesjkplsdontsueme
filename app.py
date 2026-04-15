import json     # Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")   # create variable "data" that represents the entire pokedex list
languages=["english","japanese","chinese","french"]
for index, language in enumerate(languages):
    print(index, ':', language)
lang=int(input("Please enter the index of the language you wish to select: "))    # Add a language choice feature and print the pokemons name based on the user input
if lang == "Japanese":
    for pokemon in data:
        print(pokemon["name"]["japanese"])
elif lang == "English":
    for pokemon in data:
        print(pokemon["name"]["english"])
elif lang == "French":
    for pokemon in data:
        print(pokemon["name"]["french"])
elif lang == "Chinese":
    for pokemon in data:
        print(pokemon["name"]["chinese"])
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type