import json     # Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
# create variable "data" that represents the entire pokedex list
data=json.load(pokedex)
# Add a language choice feature and print the pokemons name based on the user input
languages=["english","japanese","chinese","french"]
for language in (languages):
    print(language)
lang=input("Please enter the index of the language you wish to select: ").lower()
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
if lang == "japanese":
    for pokemon in data:
        print(pokemon["name"]["japanese"])
elif lang == "french":
    for pokemon in data:
        print(pokemon["name"]["french"])
elif lang == "chinese":
    for pokemon in data:
        print(pokemon["name"]["chinese"])
else:
    for pokemon in data:
        print(pokemon["name"]['english'])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
types=["grass","fire","water","lightning",'grass','ice','poison','dark',"ground",'rock','steel','psychic','normal','flying','dragon','fairy']
print('Types:')
for type in (types):
    print(type)
lang =input("Please enter the index of the language you wish to select: ").lower()
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type