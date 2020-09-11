class FreqAnalysis:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ## Can't remember where I found the distribution
    proabilityDict = {
        'e': .1202,
        't': .0910,
        'a': .0812,
        'o': .0768,
        'i': .0731,
        'n': .0695,
        's': .0628,
        'r': .0602,
        'h': .0592,
        'd': .0432,
        'l': .0398,
        'u': .0288,
        'c': .0271,
        'm': .0261,
        'f': .0230,
        'y': .0211,
        'w': .0209,
        'g': .0203,
        'p': .0182,
        'b': .0149,
        'v': .0111,
        'k': .0069,
        'x': .0017,
        'q': .0011,
        'j': .0010,
        'z': .0007
    }

    ## Takes each shiftcipher, and does aprediction against it
    def predictKey(self, ciphertext, keylen):
        splits = self.splitCipherText(ciphertext, keylen)
        result = ''
        for i in range(keylen):
            occurrence = self.__generateOccurrences(splits[i])
            result = result + self.__predictKeyLetter(occurrence)
        return result

    def getPredicted(self, partialciphertext):
        return self.__generatePredictionDict(partialciphertext)

    def getOccurrences(self, partialciphertext):
        return self.__generateOccurrences(partialciphertext)

    ## Splits the ciphertext into its shift ciphers
    ## based on keylen
    def splitCipherText(self, ciphertext, keylen):
        cipherTextArr = []
        for i in range(keylen):
            cipherTextArr.append(self.__splitify(ciphertext, i, keylen))
        return cipherTextArr

    ## Creates a prediction based on the dict up top,
    ## and the length of the shift ciphers text
    def __generatePredictionDict(self, shiftciphertext):
        predictionDict = {}
        for i in self.alphabet:
            predictionDict[i] = round(
                len(shiftciphertext) * self.proabilityDict[i])
        return predictionDict

    ## Generates an occurrence map based on some text
    ## in this it uses one of the derived shift ciphers
    def __generateOccurrences(self, shiftciphertext):
        occurrenceDict = {}
        for i in self.alphabet:
            occurrenceDict[i] = 0

        for i in shiftciphertext:
            occurrenceDict[i] += 1
        return occurrenceDict

    ## Takes the most occurred letter and shifts it to e
    ## then derive the number shifted and reassociate
    ## with the predicted letter
    def __predictKeyLetter(self, occurrenceDict):
        mostFrequent = 0
        approxE = ''
        for i in occurrenceDict:
            if (occurrenceDict[i] > mostFrequent):
                mostFrequent = occurrenceDict[i]
                approxE = i

        return self.__deshift(approxE)

    def __deshift(self, mostFrequent):
        return self.alphabet[self.alphabet.find(mostFrequent) - 4]

    ## Splits the text into pieces based on which
    ## letter of the key they are encrypted with
    def __splitify(self, text, start, nth):
        return text[start::nth]
