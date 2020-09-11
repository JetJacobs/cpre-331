import sys
from findkey import KeyGuess
from freqanalysis import FreqAnalysis

alphabet = 'abcdefghijklmnopqrstuvwxyz'

keyLenPredictor = KeyGuess()
analyser = FreqAnalysis()


def main():
    arguments = len(sys.argv)
    print('--------------------------------------')

    if ('--keylen' in sys.argv and arguments >= 3):
        ciphertext = loadCipherText('--keylen')
        print(keyLenPredictor.predictKeyLen(ciphertext))

    elif ('-a' in sys.argv and arguments >= 3):
        ciphertext = loadCipherText('-a')
        keylen = keyLenPredictor.predictKeyLen(ciphertext)
        splits = analyser.splitCipherText(ciphertext, keylen)

        for i in range(keylen):
            print('\t\t\t------Shift', i + 1, '------')
            printDicts(analyser.getPredicted(splits[i]),
                       analyser.getOccurrences(splits[i]))

    elif ('--key' in sys.argv and arguments >= 3):
        ciphertext = loadCipherText('--key')
        keylen = keyLenPredictor.predictKeyLen(ciphertext)

        result = analyser.predictKey(ciphertext, keylen)
        print('Guessed Key:', result)

    elif ('-s' in sys.argv and arguments >= 4):
        ciphertext = loadCipherText('-s')
        key = sys.argv[sys.argv.index('-s') + 1]

        print(shiftAll(ciphertext, key))
    elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print('Run the program with the following\n')
        print('You may read from a file using the following')
        print('Please note the filename must follow the flag imediately')
        print('\tRead From File:\t -f <filename>\n')
        print('\tPredict Key Length:\t --keylen <ciphertext>')
        print('\tFrequency Analysis:\t -a <ciphertext>')
        print('\tGuess the Key:\t\t --key <ciphertext>')
        print('\tDecode:\t\t\t -s <key> <ciphertext>')
    else:
        print('Try passing --help')


## Loads the cipher from the text file or argv depending
def loadCipherText(trigger):
    ## From https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
    ciphertext = ''
    if ('-f' in sys.argv):
        with open(sys.argv[sys.argv.index('-f') + 1]) as f:
            ciphertext = ''.join([x.strip() for x in f])
    elif (trigger == '-s'):
        ciphertext = sys.argv[sys.argv.index(trigger) + 2]
        key = sys.argv[sys.argv.index(trigger) + 1]
    else:
        ciphertext = sys.argv[sys.argv.index(trigger) + 1]

    return ciphertext


def printDicts(dict1, dict2):
    count = 0
    print("Count:\t Letter:\t Prediction:\t Actual:\t Shift\t")
    for i in alphabet:
        count += 1
        print(count, "\t", i, "\t\t", dict1[i], '\t\t', dict2[i], '\t\t',
              alphabet[alphabet.find(i) - 4])


## preforms a shift based on the key letter
def shift(letter, keyletter):
    index = alphabet.find(keyletter)
    resultIndex = (alphabet.find(letter) - index)
    if resultIndex >= len(alphabet):
        resultIndex -= 26
    return alphabet[resultIndex]


def shiftAll(ciphertext, key):
    result = ''
    for i in range(len(ciphertext)):
        result += shift(ciphertext[i], key[i % len(key)])
    return result


main()