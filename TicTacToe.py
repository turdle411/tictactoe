#tic tac toe

import turtle
import os
import array
import random

turtle.setup(550, 600)
wn = turtle.Screen()
wn.bgcolor("pink")

choose = False
single = True


player_pen = turtle.Turtle()
player_pen.speed(0)
player_pen.color("white")
player_pen.penup()
player_pen.setposition(0, 0)
playerstring = "Single or Double"
player_pen.write(playerstring, False, align="Center", font =("Comic Sans MS", 50, "normal")) 
player_pen.hideturtle()

#player option print
singleOrDouble = turtle.Turtle()
singleOrDouble.speed(0)
singleOrDouble.color("white")
singleOrDouble.penup()
singleOrDouble.setposition(-100, -55)
sodstring = "Single"
singleOrDouble.write(sodstring, False, align="Center", font =("Comic Sans MS", 22, "normal")) 
singleOrDouble.hideturtle()
singleOrDouble.penup()
singleOrDouble.setposition(100, -55)
sodstring = "Double"
singleOrDouble.write(sodstring, False, align="Center", font =("Comic Sans MS", 22, "normal")) 
singleOrDouble.hideturtle()

while (not(choose)):
    #draw options
    options_pen = turtle.Turtle()
    options_pen.speed(0)
    options_pen.color("white")
    options_pen.penup()
    options_pen.setposition(-150, -60)
    options_pen.pensize(3)
    options_pen.pendown()
    for i in range(2):
        options_pen.fd(100)
        options_pen.lt(90)
        options_pen.fd(50)
        options_pen.lt(90)
    options_pen.penup()
    options_pen.setposition(50, -60)
    options_pen.pendown()
    for i in range(2):
        options_pen.fd(100)
        options_pen.lt(90)
        options_pen.fd(50)
        options_pen.lt(90)
    options_pen.hideturtle()
    options_pen.clear()

    def option (x, y):
        global choose
        global single
        if (y > -60 and y < -10):
            if (x > -150 and x < -50):
                single = True
                choose = True
            elif (x > 50 and x < 150):
                single = False
                choose = True


    wn.onclick(option)

player_pen.clear()
singleOrDouble.clear()

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-225, -225)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4) :
    border_pen.fd(450)
    border_pen.lt(90)
    border_pen.hideturtle()

#draw rows and columns
board_pen = turtle.Turtle()
board_pen.speed(0)
board_pen.color("white")
board_pen.penup()
board_pen.setposition(-225, -75)
board_pen.pensize(3)
board_pen.pendown()
for line in range(2):
    board_pen.fd(450)
    board_pen.lt(90)
    board_pen.fd(150)
    board_pen.lt(90)
board_pen.lt(90)
board_pen.penup()
board_pen.setposition(-75, -225)
board_pen.pendown()
for line in range(2):
    board_pen.fd(450)
    board_pen.lt(-90)
    board_pen.fd(150)
    board_pen.lt(-90)
board_pen.hideturtle()


xPlayer = True
player = "X"
win = [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"]]

#draw player turn
player_pen = turtle.Turtle()
player_pen.speed(0)
player_pen.color("white")
player_pen.penup()
player_pen.setposition(-225, 240)
if (xPlayer):
    player = "X"
else:
    player = "O"
playerstring = "Player: %s" %player
player_pen.write(playerstring, False, align="Left", font =("Arial", 25, "normal"))
player_pen.hideturtle()

drawCircle = turtle.Turtle()
drawX = turtle.Turtle()

def draw_circle (x, y):
    drawCircle.color("white")
    drawCircle.pensize(3)
    drawCircle.speed(0)
    drawCircle.penup()
    drawCircle.setposition(x - 55, y + 10)
    drawCircle.setheading(90)
    for angle in range (27):
        drawCircle.hideturtle()
        drawCircle.pendown()
        drawCircle.lt(-16)
        drawCircle.fd(16.25)

def draw_x (x, y):
    drawX.color("white")
    drawX.pensize(3)
    drawX.speed(0)
    drawX.penup()
    drawX.hideturtle()
    drawX.setposition(x - 60, y + 60)
    drawX.setheading(-45)
    drawX.pendown()
    drawX.fd(170)
    drawX.penup()
    drawX.setposition(x - 60, y - 60)
    drawX.pendown()
    drawX.setheading(45)
    drawX.fd(170)
    
pressed = [False, False, False, False, False, False, False, False, False]
valid = True
row = 3
col = 3

#checks rows
def checkRow (who, x, y):
    for i in range(row):
        if (not(win[i][y] == who)):
            return False
    return True

#checks columns
def checkCol (who, x, y):
    for i in range(col):
        if (not(win[x][i] == who)):
            return False
    return True

#checks diagonals
def checkDiag (who):
    diag = True
    for i in range(row):
        if (not(win[i][i] == who)):
            diag = False
    if (not(diag)):
        diag = True
        for i in range(row):
            if (not(win[i][row - 1 - i] == who)):
                diag = False
    return diag

#checks all rows, columns and diagonals
def winCheck (who):
    j = 0
    for i in range (row):
        if(checkCol(who, i, j) or checkRow(who, j, i)):
            return True
    return checkDiag(who)

plays = 0
compTurn = False

arr = [0, 0]

def checkMoveRow():
    which = "a"
    if xPlayer:
        which = "O"
    else:
        which = "X"
    for i in range(row):
        for j in range(col):
            if (win[i][j] == "A"):
                win[i][j] = which
                if(checkRow(which, i, j)):
                    win[i][j] = "A"
                    arr[0] = i
                    arr[1] = j
                    return True
                win[i][j] = "A"
    return False

def checkMoveCol():
    which = "A"
    if xPlayer:
        which = "O"
    else:
        which = "X"
    for i in range(row):
        for j in range(col):
            if (win[j][i] == "A"):
                win[j][i] = which
                if(checkCol(which, j, i)):
                    win[j][i] = "A"
                    arr[0] = j
                    arr[1] = i
                    return True
                win[j][i] = "A"
    return False

def checkMoveDiag():
    which = "A"
    if xPlayer:
        which = "O"
    else:
        which = "X"
    for i in range(row):
        if (win[i][i] == "A"):
            win[i][i] = which
            if(checkDiag(which)):
                win[i][i] = "A"
                arr[0] = i
                arr[1] = i
                return True
            win[i][i] = "A"
    for i in range(row):
        if (win[i][row - 1 - i] == "A"):
            win[i][row - 1 - i] = which
            if(checkDiag(which)):
                win[i][row - 1 - i] = "A"
                arr[0] = i
                arr[1] = row - 1 - i
                return True
            win[i][row - 1 - i] = "A"
    return False

def compChoice ():
    good = False
    goodMove = True
    global xPlayer
    xPlayer = not(xPlayer)
    if (goodMove):
        if (checkMoveRow()):
                numX = arr[0]
                numY = arr[1]
                print("row", numX, "and", numY)
                good = True    
                xPlayer = not(xPlayer)
                clickWin(numX, numY)
        elif (checkMoveCol()):
                numX = arr[0]
                numY = arr[1]
                print("col", numX, "and", numY)
                good = True
                xPlayer = not(xPlayer)
                clickWin(numX, numY)
        elif (checkMoveDiag()):
                numX = arr[0]
                numY = arr[1]
                print("diag",numX, "and" ,numY)
                good = True
                xPlayer = not(xPlayer)
                clickWin(numX, numY)
        if (not(good)):
            goodMove = False
            xPlayer = not(xPlayer)
    if (not(goodMove)):
        while(not(good)):
            if (checkMoveRow()):
                numX = arr[0]
                numY = arr[1]
                print("row", numX, "and", numY)
                good = True    
                clickWin(numX, numY)
            elif (checkMoveCol()):
                numX = arr[0]
                numY = arr[1]
                print("col", numX, "and", numY)
                good = True
                clickWin(numX, numY)
            elif (checkMoveDiag()):
                numX = arr[0]
                numY = arr[1]
                print("diag",numX, "and" ,numY)
                good = True
                clickWin(numX, numY)
            else:
                numX = random.randint(0, 2)
                numY = random.randint(0, 2)
                if (clickWin(numX, numY) == True):
                        good = True
            
#sets values for winning input and checks for winner
def winInput (x, y):
    global compTurn
    compTurn = not(compTurn)
    global xPlayer
    if (xPlayer):
        win[x][y] = "X"
        if (plays > 4 and winCheck("X")):
            player_pen.color("red")
            player_pen.penup()
            player_pen.setposition(0, 0)
            playerstring = "Player %s wins" %player
            player_pen.write(playerstring, False, align="Center", font =("Comic Sans MS", 60, "normal")) 
        else:
            xPlayer = not(xPlayer)
            output()   
            if (single and compTurn and not(plays == 9)):
                compChoice()
    elif (not(xPlayer)):
        win[x][y] = "O"
        if (plays > 4 and winCheck("O")):
            player_pen.color("red")
            player_pen.penup()
            player_pen.setposition(0, 0)
            playerstring = "Player %s wins" %player
            player_pen.write(playerstring, False, align="Center", font =("Comic Sans MS", 60, "normal")) 
        else:
            xPlayer = not(xPlayer)
            output()   
            if (single and compTurn and not(plays == 9)):
                compChoice()
    if (plays == 9 and not(winCheck("O")) and not(winCheck("X"))):
            player_pen.color("red")
            player_pen.penup()
            player_pen.setposition(0, 0)
            playerstring = "Tie"
            player_pen.write(playerstring, False, align="Center", font =("Comic Sans MS", 60, "normal")) 

def output ():
    global player
    player_pen.clear()
    if (xPlayer):
        player = "X"
    else:
        player = "O"
    playerstring = "Player: %s" %player
    player_pen.write(playerstring, False, align="Left", font =("Arial", 25, "normal"))

def clickWin (x, y):
    global plays
    global valid
    valid = False
    x1 = 0
    y1 = 0
    print ("single:", single, "x: ", x, "y: ", y, "comp: ", compTurn)
    if (((not(compTurn) or not(single)) and x > -225 and x < -75) or (single and compTurn and x == 0)):
        print("entered x 0")
        x = -150
        if (((not(compTurn) or not(single))and y < 225 and y > 75) or (single and compTurn and y == 0)):
            print("entered y 0", pressed[0])
            if (not(pressed[0])):
                print("hi", "pressed 0")
                y = 150
                pressed[0] = True
                valid = True
                x1 = 0
                y1 = 0
        elif (((not(compTurn) or not(single)) and y < 75 and y > -75) or (single and compTurn and y == 1)):
            print("entered y 3", pressed[3])
            if (not(pressed[3])):
                print("hi", "pressed 3")
                y = 0
                pressed[3] = True
                valid = True
                x1 = 0
                y1 = 1
        elif (((not(compTurn) or not(single)) and y < -75 and y > -225) or (single and compTurn and y == 2)):
            print("entered y 6", pressed[6])
            if (not(pressed[6])):
                print("hi", "pressed 6")
                y = -150
                pressed[6] = True
                valid = True
                x1 = 0
                y1 = 2
    elif (((not(compTurn) or not(single)) and x > -75 and x < 75) or (single and compTurn and x == 1)):
        print("entered x")
        x = 0
        if (((not(compTurn) or not(single)) and y < 225 and y > 75) or (single and compTurn and y == 0)):
            print("entered y 1", pressed[1])
            if (not(pressed[1])):
                print("hi", "pressed 1")
                y = 150
                pressed[1] = True
                valid = True
                x1 = 1
                y1 = 0
        elif (((not(compTurn) or not(single)) and y < 75 and y > -75) or (single and compTurn and y == 1)):
            print("entered y 4", pressed[4])
            if (not(pressed[4])):
                print("hi", "pressed 4")
                y = 0
                pressed[4] = True
                valid = True
                x1 = 1
                y1 = 1
        elif (((not(compTurn) or not(single)) and y < -75 and y > -225) or (single and compTurn and y == 2)):
            print("entered y 7", pressed[7])
            if (not(pressed[7])):
                print("hi", "pressed 7")
                y = -150 
                pressed[7] = True
                valid = True
                x1 = 1
                y1 = 2
    elif (((not(compTurn) or not(single)) and x > 75 and x < 225) or (single and compTurn and x == 2)):
        print("entered x")
        if (compTurn):
            print("second row")
        x = 150
        if (((not(compTurn) or not(single)) and y < 225 and y > 75) or (single and compTurn and y == 0)):
            print("entered y 2", pressed[2])
            if (not(pressed[2])):
                print("hi", "pressed 2")
                y = 150
                pressed[2] = True
                valid = True
                x1 = 2
                y1 = 0
        elif (((not(compTurn) or not(single)) and y < 75 and y > -75) or (single and compTurn and y == 1)):
            print("entered y 5", pressed[5])
            if (not(pressed[5])):
                print("hi", "pressed 5")
                y = 0
                pressed[5] = True
                valid = True
                x1 = 2
                y1 = 1
        elif (((not(compTurn) or not(single)) and y < -75 and y > -225) or (single and compTurn and y == 2)):
            print("entered y 8", pressed[8])
            if (not(pressed[8])):
                print("hi", "pressed 8")
                y = -150 
                pressed[8] = True
                valid = True
                x1 = 2
                y1 = 2

    print(plays, "out", valid, x, y)

    global xPlayer
    if (xPlayer and valid):
        draw_x(x, y)
        plays += 1
        winInput(x1, y1)
    elif (not(xPlayer) and valid):
        draw_circle(x, y)
        plays += 1
        winInput(x1, y1)
    return valid
      
wn.onclick(clickWin)

delay = input("Press enter to finish")