import random

def generateDrawingOfPowerball():
    whiteballs = []
    while(len(whiteballs) < 5):
        newball = random.randint(1, 69)
        if(newball not in whiteballs):
            whiteballs.append(newball)
        
    redball = random.randint(1, 26)

    return whiteballs, redball

def predictDrawing(previousdraw):
    random.seed(1)
    currDraw = [0, 1]
    
    while(previousdraw[0] != currDraw[0] or previousdraw[1] != currDraw[1]):
        currDraw = generateDrawingOfPowerball()
    
    whiteballs, redball = generateDrawingOfPowerball()
    return whiteballs, redball

def predictDrawingByNumber(drawing):
    random.seed(1)
    
    for i in range(1, drawing):
        generateDrawingOfPowerball()
    
    whiteballs, redball = generateDrawingOfPowerball()
    return whiteballs, redball

def printBalls(balls, drawing):
    print('----Drawing', drawing, '----')
    print('White balls:', 
        balls[0][0], 
        balls[0][1], 
        balls[0][2], 
        balls[0][3], 
        balls[0][4],
        'Red Ball:', balls[1])
    print('\n')




if __name__ == "__main__":

    print('######## Prediction for draw ########')
    printBalls(predictDrawingByNumber(11), 11)

    print('###### Powerball generator ######')
    random.seed(1)
    for i in range(1, 11):
        drawing = generateDrawingOfPowerball()
        printBalls(drawing, i)

    print('########## Predicted Drawing! ##########')
    printBalls(generateDrawingOfPowerball(), 11)

    print('Draw Prediction based on previous draw')
    printBalls(predictDrawing(drawing), 11)



    
