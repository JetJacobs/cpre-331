class Rotor:
    order = []
    reset = ['']
    position = 0

    def __init__(self, position, key):
        self.deriveOrder(key)
        self.reset = self.order.copy()
        self.position = position

    def deriveOrder(self, key):
        length = len(key)
        neworder = []
        for x in range(length):
            neworder.append(key[x])
        self.order = neworder

    def getDisplay(self):
        return self.order[self.position]

    def findRotation(self, char):
        rotation = 0

        for x in range(len(self.order)):
            if (self.order[x] == char):
                if (x - self.position < 0):
                    rotation = 26 - (self.position - x)
                    break
                else:
                    rotation = x - self.position
                    break
        return rotation

    def rotate(self, rotation):
        self.position += rotation
        if (self.position >= 26):
            self.position = self.position % 26
        if (self.position < 0):
            self.position = 26 + -(26 % abs(self.position))

    def flip(self):
        oppositeIndex = self.findOpposite(self.position)
        oppositeChar = self.order[oppositeIndex]
        self.order[oppositeIndex] = self.getDisplay()
        self.order[self.position] = oppositeChar

    def kick(self, toRight):
        if (toRight):
            lastchar = self.order.pop()
            self.order.insert(0, lastchar)
        else:
            lastchar = self.order.pop(0)
            self.order.append(lastchar)

    def findOpposite(self, pos):
        if (pos >= 13):
            return pos % 13
        else:
            return pos + 13

    def resetRotor(self):
        self.order = self.reset
