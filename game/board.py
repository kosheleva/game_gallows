from functools import partial

""" Class Board - responsible to control GUI and game itself. """
class Board:
    def __init__(self, GUI, Alphabet, Word, Gallows, config):
        """ GUI settings """
        self.gui = GUI(
            config["board"]["width"],
            config["board"]["height"],
            config["board"]["title"],
            config["board"]["opacity"],
            config["board"]["bgColorLight"]
        )
        """ Creating additional objects """
        self.alphabet = Alphabet()
        self.word = Word()
        self.gallows = Gallows()

        self.config = config


    """ Window with game rules """   
    def openRules(self):
        self.gui.createPopup("Game rules", """
A word and one or more clue letters are given. The player suggests a letter that can be included in this word.
If such a letter is in a word, it appears in the word - as many times as it occurs in the word.
If there is no such letter, then a part is drawn to the gallows. The player continues to guess the letters until he guesses the whole word.
For each wrong answer, one part of the body is added to the gallows.
If the body in the gallows is drawn completely, then the player has lost and can start the game again.
        """)


    """ Switch to light mode """  
    def setLightMode(self):
        self.gui.setWindowBackgroundColor(self.config["board"]["bgColorLight"])


    """ Switch to dark mode """ 
    def setDarkMode(self):
        self.gui.setWindowBackgroundColor(self.config["board"]["bgColorDark"])


    """ Close the game by clicking on cross icon """
    def close(self):
        self.gui.closeWindow()
    

    """ Show game menu """
    def drawMenu(self):
        menu = self.gui.openFrame(
            self.config["menuFrame"]["width"],
            self.config["menuFrame"]["height"],
            self.config["menuFrame"]["bgColor"]
        )

        self.menuFrame = menu

        icons = [
            { "icon": self.config["menuFrame"]["rulesIconCode"], "handler": self.openRules },
            { "icon": self.config["menuFrame"]["lightModeIconCode"], "handler": self.setLightMode },
            { "icon": self.config["menuFrame"]["darkModeIconCode"], "handler": self.setDarkMode },
            { "icon": self.config["menuFrame"]["closeIconCode"], "handler": self.close }
        ]

        for i in range(len(icons)):
          self.gui.createButton(
            menu, 
            self.config["button"]["size"], 
            icons[i]["icon"], 
            self.config["button"]["contentPadx"], 
            self.config["button"]["contentPady"], 
            self.config["button"]["padx"], 
            self.config["button"]["pady"], 
            self.config["button"]["width"], 
            self.config["button"]["height"], 
            self.config["button"]["highlightbackground"], 
            self.config["button"]["side"], 
            icons[i]["handler"]
        )
        
        self.gui.packFrame(
            menu, 
            self.config["menuFrame"]["side"], 
            self.config["menuFrame"]["padx"], 
            self.config["menuFrame"]["pady"])


    """ Draw a gallow """
    def drawGallows(self):
        canvas = self.gui.createCanvas(self.config["gallowsFrame"]["width"], self.config["gallowsFrame"]["height"], self.config["gallowsFrame"]["bgColor"])
        self.canvas = canvas

        coords = self.gallows.getGallowsCoords()
        for item in coords:
            self.gui.drawLine(canvas, item["x1"], item["y1"], item["x2"], item["y2"], self.config["gallowsFrame"]["color"], 5)

        self.gallowsFrame = canvas

    
    """ Update the hidden word """
    def updateWord(self, frame, word):
        for child in frame.winfo_children():
            child.destroy()

        for item in word:
            self.gui.createLabel(frame, item, self.config["label"]['side'], self.config["label"]['padx'], self.config["label"]['pady'], self.config["label"]['bgColor'])


    """ Update the gallow  """
    def updateGallow(self):
        self.gallowsFrame.delete("all")
        self.gallows.resetGallow()

        coords = self.gallows.getGallowsCoords()
        for item in coords:
            self.gui.drawLine(self.gallowsFrame, item["x1"], item["y1"], item["x2"], item["y2"], 'black', 5)
            
    
    """ Handle choosing a letter """
    def chooseLetterHandler(self, letter):
        indexes = self.word.checkLetter(letter)
        isLetterCorrect = len(indexes)

        """ 
        If the letter is guessed, write it in a word and check whether the whole word is guessed, if so -
        we show the winning window, update the word and gallow
        """
        if isLetterCorrect:
            updatedTask = self.word.fillLetter(letter, indexes)
            self.updateWord(self.wordFrame, updatedTask)
        
            isTaskDone = self.word.isTaskDone()

            if isTaskDone:
                self.gui.createPopup("Wow!", "You won!")

                newTask = self.word.createNewTask()
                self.updateWord(self.wordFrame, newTask)

                self.updateGallow()       
        else:
            """ 
            If the letter is not guessed, we update the gallow
            and check if there are more attempts, if not - update the game with a new word
            """
            nextPart = self.gallows.getNextBodyPart()

            if nextPart["id"] == 'head' and not nextPart["isDone"]:
                self.gui.drawCircle(self.canvas, nextPart["coords"]["x1"], nextPart["coords"]["y1"], nextPart["coords"]["x2"], nextPart["coords"]["y2"], self.config["gallowsFrame"]["fillColor"], 5, self.config["gallowsFrame"]["outlineColor"])
            elif nextPart["id"] in ['body', 'left_hand', 'right_hand', 'left_leg', 'right_leg'] and not nextPart["isDone"]:
                self.gui.drawLine(self.canvas, nextPart["coords"]["x1"], nextPart["coords"]["y1"], nextPart["coords"]["x2"], nextPart["coords"]["y2"], '#000000', 5)
            else:
                self.gui.drawLine(self.canvas, nextPart["coords"]["x1"], nextPart["coords"]["y1"], nextPart["coords"]["x2"], nextPart["coords"]["y2"], '#000000', 5)

            if nextPart["isDone"]:            
                self.updateGallow()
                newTask = self.word.createNewTask()
                self.updateWord(self.wordFrame, newTask)
        

    """ Display the hidden word """ 
    def drawWord(self):
        task = self.word.generateTask()

        word = self.gui.openFrame(self.config["wordFrame"]["width"], 60, self.config["wordFrame"]["bgColor"])
        
        for i in range(len(task)):
            self.gui.createLabel(word, task[i], self.config["label"]['side'], self.config["label"]['padx'], self.config["label"]['pady'], self.config["label"]['bgColor'])
        
        self.gui.packFrame(word, 'top', 10, 30)

        self.wordFrame = word
    

    """ Display letters """ 
    def drawAlphabet(self):
        letters = self.alphabet.getLetters()
        
        for i in range(len(letters)):
            lettersFrame = self.gui.openFrame(self.config["alphabetFrame"]["width"], self.config["alphabetFrame"]["height"], self.config["alphabetFrame"]["bgColor"])
            for j in range(len(letters[i])):
                self.gui.createButton(
                    lettersFrame, 
                    self.config["letterBtn"]["size"], 
                    letters[i][j], 
                    self.config["letterBtn"]["contentPadx"], 
                    self.config["letterBtn"]["contentPady"], 
                    self.config["letterBtn"]["padx"], 
                    self.config["letterBtn"]["pady"], 
                    self.config["letterBtn"]["width"], 
                    self.config["letterBtn"]["height"], 
                    self.config["letterBtn"]["highlightbackground"], 
                    self.config["letterBtn"]["side"],
                    partial(self.chooseLetterHandler, letters[i][j])
                )
            self.gui.packFrame(lettersFrame, 'top', 10, 0)
        

    """ Run the game """ 
    def run(self):
        self.drawMenu()
        self.drawGallows()
        self.drawWord()
        self.drawAlphabet()
        
        self.gui.display()



    