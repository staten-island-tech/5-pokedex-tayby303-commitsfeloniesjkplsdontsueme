import json     # Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
# create variable "data" that represents the entire pokedex list
data=json.load(pokedex)
# Add a language choice feature and print the pokemons name based on the user input
languages=["english","japanese","chinese","french"]
for language in (languages):
    print(language)
lang=input("Please enter the language you wish to select: ").lower()
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
for pokemon in data:
    print(pokemon['name'][lang])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def typeSearch():
    type1=input("What pokemon type are you searching for? ").capitalize()
    t2=input("Is there a secondary typing? yes/no ").lower()
    if t2=='yes':
        type2=input("What pokemon type are you searching for? ").capitalize()
        for pokemon in data:
            if type1 in pokemon["type"] and type2 in pokemon["type"]:
                print(pokemon["name"][lang])
    elif t2!='yes':
        for pokemon in data:
            if type1 in pokemon["type"]:
                print(pokemon["name"][lang])
#typeSearch()
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.
def nameSearch():
    mon = input("Would you like to search for a pokemon?: ").capitalize()
    while mon == "Yes":
        user_search = input(" Search for a Pokemon here: ")
        for poke_names in data:
            if user_search in poke_names["name"][lang]:
                print(poke_names["name"][lang])
nameSearch()
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type
