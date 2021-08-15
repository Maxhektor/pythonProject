from anObject import anObject

class anObjectChild(anObject):
    def __init__(self):
        anObject.__init__(self)
        self.property3 = "Third property of our object"

