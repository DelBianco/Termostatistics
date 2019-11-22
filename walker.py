import random

class Walker:
    def __init__(self, x, d = 1):
        self.x = x
        self.d = d

    def __str__(self):
        return str(self.x)

    def getX(self):
        return self.x

    def walk(self):
        val = random.randint(0,2)
        if(val == 0):
            self.x = self.x + self.d
        elif(val == 1):
            self.x = self.x - self.d

        return self
