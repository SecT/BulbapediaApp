__author__ = 'Grzesiek'

class PokemonListParseProcessor:


    def __init__(self):
        self.state = "start"
        self.pokemonURLs = []

    #states:  start, h3, table, a

    def changeState(self, tag):
    #     if tag == "h4" and self.state == 0:
    #         self.state = 1
    #
    #     if tag == "tr" and self.state == 2:
    #         self.state = 3
        if tag == "h3" and self.state == "start":
            self.state = "h3Begin"

        # if tag == "table" and self.state == "h3Begin":
        #    self.state = "tableBegin"

        if tag == "tr" and self.state == "h3Begin":
            self.state = "trBegin"


        if tag == "a" and self.state  == "trBegin":
            self.state = "aBegin"


    def backState(self,tag):
        if tag == "a" and self.state == "aBegin":
            self.state = "h3Begin"

    def process(self, data):
        if self.state == "aBegin":

            #if data[0] == "href":
            if data[0][0] == "href":
                self.pokemonURLs.append(data[0][1])
            return True
        # if self.state == 1:
        #     if data == "breeding":
        #         self.state = 2
        #
        # if self.state == 3:

        return False
