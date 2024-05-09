class Alphabet:
    def __init__(self):
        """ Letters """
        self.letters = [
            [ "A", "B", "C", "D", "E" ],
            [ "F", "G", "H", "I", "J" ],
            [ "K", "L", "M", "N", "O" ],
            [ "P", "Q", "R", "S", "T" ],
            [ "U", "V", "W", "X", "Y" ],
            [ "Z" ]
        ]


    """ Get available letters """
    def getLetters(self):
        return self.letters
