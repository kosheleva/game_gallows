import random

""" Class for working with a hidden word """
class Word:
    def __init__(self):
        """ Random words to display as a hidden word """
        self.randomWords = [
            "BOOK",
            "HOUSE",
            "AUTUMN",
            "APPLE",
            "CHAIR",
            "CAR",
            "TOY",
            "CAT",
            "NOTEBOOK",
            "TREE",
            "GAME",
            "PENCIL",
            "FLOWER",
            "MOUSE",
            "GARDEN",
        ]

        self.init()


    """ Choose hidden word """
    def init(self):
        self.word = random.choice(self.randomWords)
        self.task = []


    """ Add clue-letters and format a hidden word """
    def generateTask(self):
        if len(self.task):
            return self.task
        
        task = [None] * len(self.word)

        task[0] = self.word[0]
        task[int(len(self.word)-1)] = self.word[int(len(self.word)-1)]

        self.task = task

        return task
                    

    """ Check if hidden word contains choosed letter """
    def checkLetter(self, letter):
        indexes = []

        for i in range(len(self.word)):
            if (self.word[i] == letter):
                indexes.append(i)

        return indexes
    

    """ Add correct letter to hidden word """
    def fillLetter(self, letter, indexes):
        for i in indexes:
            self.task[i] = letter
 
        return self.task


    """ Check if the whole word is guessed """
    def isTaskDone(self):
        for item in self.task:
            if not item: 
                return False
            
        return True
    

    """ Create new hidden word """
    def createNewTask(self):
        self.init()
        task = self.generateTask()
        return task



    