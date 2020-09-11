import sys
from rotor import Rotor


def main():
    arguments = len(sys.argv) - 1
    leftRotor = Rotor(0, 'abcdefghijklmnopqrstuvwxyz')
    if (sys.argv[1] == '-e' and arguments >= 2):
        rightRotor = Rotor(0, 'tlmvpcbsuofnaqdhweiyrjzxgk')

        ciphertext = encode(sys.argv[2], leftRotor, rightRotor)
        key = ''
        print(ciphertext + ' ' + key.join(rightRotor.order))
    elif (sys.argv[1] == '-d' and arguments >= 3):
        rightRotor = Rotor(0, sys.argv[3])

        plaintext = decode(sys.argv[2], leftRotor, rightRotor)
        print(plaintext[::-1])
    elif (sys.argv[1] == '--test' and arguments == 1):
        testRun()
    elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print('There are only three ways to run this program')
        print('\tEncrypt:\t -e <plaintext>')
        print('\tDecrypt:\t -d <ciphertext> <key>')
        print('\tTestConfig:\t -test')
    else:
        print('Try passing --help')


def encode(plaintext, leftRotor, rightRotor):
    ciphertext = ''
    plaintext = plaintext.replace(' ', '')
    plaintext = plaintext.lower()
    length = len(plaintext)
    for char in range(length):
        ciphertext += encodeChar(plaintext[char], leftRotor, rightRotor)
        rightRotor.flip()
        rightRotor.kick(True)
        #print(rightRotor.order)

    return ciphertext


def encodeChar(char, leftRotor, rightRotor):
    rotation = leftRotor.findRotation(char)
    leftRotor.rotate(rotation)
    rightRotor.rotate(rotation)
    return rightRotor.getDisplay()


def decode(ciphertext, leftRotor, rightRotor):
    plaintext = ''
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = ciphertext.lower()
    length = len(ciphertext)
    for char in range(length):
        plaintext += decodeChar(ciphertext[(length - 1) - char], leftRotor,
                                rightRotor)

    return plaintext


def decodeChar(char, leftRotor, rightRotor):
    rightRotor.kick(False)
    rotation = rightRotor.findRotation(char)
    rightRotor.rotate(rotation)
    leftRotor.rotate(rotation)
    rightRotor.flip()

    rotation = rightRotor.findRotation(char)
    rightRotor.rotate(rotation)
    leftRotor.rotate(rotation)
    return leftRotor.getDisplay()


def testRun():
    rightRotor = Rotor(0, 'tlmvpcbsuofnaqdhweiyrjzxgk')

    ciphertext = encode("my message", leftRotor, rightRotor)
    print(leftRotor.order)
    plaintext = decode(ciphertext, leftRotor, rightRotor)

    print(plaintext[::-1])
    key = ''
    print(ciphertext + ' ' + key.join(rightRotor.order))


main()
