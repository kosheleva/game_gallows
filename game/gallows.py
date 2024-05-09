class Gallows:
    def __init__(self):
        """ Coordinates of the gallow """ 
        self.gallows = [
            { "x1": 30, "y1": 30, "x2": 30, "y2": 300 },
            { "x1": 30, "y1": 30, "x2": 150, "y2": 30 },
            { "x1": 150, "y1": 30, "x2": 30, "y2": 80 },
            { "x1": 150, "y1": 30, "x2": 150, "y2": 80 },
        ]

        """ Coordinates of the body """ 
        self.body = {
            "head": { "x1": 120, "y1": 60, "x2": 180, "y2": 120 },
            "body": { "x1": 150, "y1": 120, "x2": 150, "y2": 230 },
            "left_hand": { "x1": 150, "y1": 150, "x2": 100, "y2": 200 },
            "right_hand": { "x1": 150, "y1": 150, "x2": 200, "y2": 200 },
            "left_leg": { "x1": 150, "y1": 230, "x2": 100, "y2": 300 },
            "right_leg": { "x1": 150, "y1": 230, "x2": 200, "y2": 300 }
        }

        """ Sequence of what to draw after wrong letter """ 
        self.partsToDraw = ["head", "body", "left_hand", "right_hand", "left_leg", "right_leg"]
        

    """ Get gallow coordinates """
    def getGallowsCoords(self):
        return self.gallows
    

    """ Get coordinates of next part of the body """
    def getNextBodyPart(self):
        id = self.partsToDraw.pop(0)
        return { "id": id, "coords": self.body[id], "isDone": not len(self.partsToDraw) }
    

    """ Update gallow """
    def resetGallow(self):
        self.partsToDraw = ["head", "body", "left_hand", "right_hand", "left_leg", "right_leg"]

        
                    

    





    