from math import gcd


class KeyGuess:
    cipherText = ''
    startDict = {}
    distDict = {}
    divisorsDict = {}

    def predictKeyLen(self, ciphertext):
        self.__generateStartDict(self.startDict, ciphertext)
        self.__generateDistDict(self.startDict, self.distDict)
        result = self.__findMostFrequentGCD(self.distDict)
        return result

    def __findMostFrequentGCD(self, distdict):
        self.divisorsDict = {}
        for i in distdict:
            divisor = self.__getDivisors(distdict[i])
            if divisor != 1:
                if divisor in self.divisorsDict:
                    self.divisorsDict[divisor] += 1
                else:
                    self.divisorsDict[divisor] = 1

        mostFrequent = 0
        for i in self.divisorsDict:
            if (self.divisorsDict[i] > mostFrequent):
                mostFrequent = i

        return mostFrequent

    ## So basically this goes through and finds all recurring substrings
    ## with length greater than 2 since random occurrences of two are likely.
    ##
    ## From there it stores them using the string as the key and an array
    ## of startpoints as the value
    def __generateStartDict(self, dictionary, ciphertext):
        for i in range(len(ciphertext) - 5):
            temp = []
            for j in range(3, 7):
                substring = ciphertext[i:i + j]
                temp = [(x) for x in self.__findAll(ciphertext, substring)]
                if len(temp) >= 2:
                    if substring not in dictionary:
                        dictionary[substring] = [
                            (x) for x in self.__findAll(ciphertext, substring)
                        ]

    ## This goes throught the list of start points for repeated elements
    ## then makes a dict for only the distances between them.
    def __generateDistDict(self, dictIn, dictOut):
        for i in dictIn:
            startarr = dictIn[i]
            arrlen = len(startarr) - 1
            distarr = []
            for j in range(arrlen):
                distarr.append((startarr[j + 1] - startarr[j]))
            if len(distarr) > 1:
                dictOut[i] = distarr
            distarr = []

    def __printDict(self, dictionary):
        for x in dictionary:
            print(x, dictionary[x])

    ## Inspired by a solution at
    ## stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
    def __findAll(self, string, substring):
        firstoccurrence = string.find(substring)
        while firstoccurrence != -1:
            yield firstoccurrence + 1
            firstoccurrence = string.find(substring, firstoccurrence + 1)

    ## Pulled from https://www.geeksforgeeks.org/common-divisors-of-n-numbers/
    def __getDivisors(self, arr):

        # Variable to find the gcd
        # of N numbers
        g = arr[0]

        # Set to store all the
        # common divisors
        divisors = dict()

        # Finding GCD of the given
        # N numbers
        for i in range(1, len(arr)):
            g = gcd(arr[i], g)
        return g