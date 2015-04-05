__author__ = 'Grzesiek'


import urllib.request

from MyHTMLParser import MyHTMLParser

#page - A Pokemon page from Bulbapedia in the HTML format
#If the Pokemon has egg moves that can only be learned from a Pokemon from generation III, IV or V, return a link to its page
def checkEggMovesFromPrevGeneration(page):
    if page.decode('utf-8').count("‡") > 1:
        return link
    return False

#Returns a list of partial URLs to all Pokemon pages from Bulbapedia.
#Sample element: "/wiki/Charmander_(Pok%C3%A9mon)"
#To obtain a complete URL, append each element to "http://bulbapedia.bulbagarden.net"
#The elements are ordered according to National Pokedex number
#The list is obtained from http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number
def getListOfPokemonPages():

    pokemonListAddress = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

    pokeListResponse = urllib.request.urlopen(pokemonListAddress)
    pokeListPage = str(pokeListResponse.read())

    parser = MyHTMLParser()
    parser.feed(pokeListPage)

    return  parser.pokeListParser.pokemonURLs



####################

listOfPokemonPages = getListOfPokemonPages()
print(listOfPokemonPages)


baseBulbapediaAdress = "http://bulbapedia.bulbagarden.net"

downloadedPagesLimit = len(listOfPokemonPages)
start = 0

for link in listOfPokemonPages[start:start+downloadedPagesLimit]:
    response = urllib.request.urlopen(baseBulbapediaAdress+link)
    page = response.read()

    data = checkEggMovesFromPrevGeneration(page)
    if data != False:
        print("Found: " + data)


print("End")