__author__ = 'Grzesiek'

from html.parser import HTMLParser
from  PokemonListParseProcessor import PokemonListParseProcessor

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.pokeListParser = PokemonListParseProcessor()

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if tag == "tr" or tag == "h3" or tag == "table":
            self.pokeListParser.changeState(tag)

        if tag == "a":
            self.pokeListParser.changeState(tag)
            self.pokeListParser.process(attrs)
        return True

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        if tag == "a":
            self.pokeListParser.backState(tag)

        return True

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        self.pokeListParser.process(data)