import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# Add a language choice feature and print the pokemons name based on the user input
lan_choice = ("")
x = ("")
def print_pokemon_names(data):
    lan_choice = input("What laguage do you want: Japanese, English, French, or Chinese? ")
    x = lan_choice.capitalize()
    if x == "Japanese":
        for pokemon in data:
            print(pokemon["name"]["japanese"])
    elif x == "English":
        for pokemon in data:
            print(pokemon["name"]["english"])
    elif x == "French":
        for pokemon in data:
            print(pokemon["name"]["french"])
    elif x == "Chinese":
        for pokemon in data:
            print(pokemon["name"]["chinese"])
print_pokemon_names(data)

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

def type_list():
    type_choice = input("What pokemon type are you searching for? ")
    x = type_choice.capitalize()
    found = False
    for pokemon in data:
        if x in pokemon["type"]:
            found = True
            print(pokemon["name"]["english"])
    if found  == False:    
        print("No pokemon of that type was found.")
type_list()
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

def poke_search():
    continue_search = input("Would you like to search for a pokemon?: ")
    y = continue_search.capitalize()
    while y == "Yes":
        user_search = input(" Search for a Pokemon here: ")
        for poke_names in data:
            if user_search in poke_names["name"]["english"]:
                print(poke_names["name"]["english"])
poke_search()
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type