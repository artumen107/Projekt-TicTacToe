import pygame as pg
import sys
import time
from datetime import datetime
from pygame.locals import *

# LOADING PERSONALIZATION SETTINGS FROM FILES @@@
Fcolor = open("C:/TicTacToe/Kolor.txt")
FName1 = open("C:/TicTacToe/Name1.txt")
FName2 = open("C:/TicTacToe/Name2.txt")
FStartingPlayer = open("C:/TicTacToe/Zaczynajacy.txt")

color = Fcolor.read().replace(" ", "").replace("\n", "")
name1 = FName1.read().replace(" ", "").replace("\n", "")
name2 = FName2.read().replace(" ", "").replace("\n", "")
StartingPlayerSymbol = FStartingPlayer.read().replace(" ", "").replace("\n", "")

if StartingPlayerSymbol == "O":
    SecondPlayerSymbol="X"
    StartingPlayerSymbol="O"
    print("Gracz startujacy: " + StartingPlayerSymbol)
else:
    SecondPlayerSymbol="O"
    StartingPlayerSymbol="X"
    print("Gracz startujacy: " + StartingPlayerSymbol)


#    *** Main settings ***

# wall and rules
WhoseTurn = StartingPlayerSymbol
TheWinner = None
Draw = False

# the board
Width = 400
Height = 400
Board = [[None] * 3, [None] * 3, [None] * 3]

# some colors variables to make it easier later
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 191, 255)



# counting points to show a result

FirstPlayerPoints = 0
SecondPlayerPoints = 0

# APP GUI settings

x = pg.init()  # make able to use the pygame package
FPS = 30
TimeClock = pg.time.Clock()
MainDisplay = pg.display.set_mode((Width, Height + 180), 0, 32, 0, 0)
pg.display.set_caption("Tic Tac Toe Artur Mendela", "Tic Tac Toe Artur Mendela")

StartingBoard = pg.image.load("StartBoard.jpg")
ImageOfX = pg.image.load("ImageOfX.jpg")
ImageOfO = pg.image.load("ImageOfO.jpg")

StartingBoard = pg.transform.scale(StartingBoard, (Width, Height + 180))
ImageOfX = pg.transform.scale(ImageOfX, (80, 80))
ImageOfO = pg.transform.scale(ImageOfO, (80, 80))


# *** several functions ***

def CreateBoard():
    global color
    MainDisplay.blit(StartingBoard, (0, 0))
    pg.display.update()
    time.sleep(1)


    if color == "blue":
        MainDisplay.fill(blue)
        print("Kolor planszy: " + color)
    else:
        print("Kolor planszy: " + color)
        MainDisplay.fill(white)

    # * draw a grid *

    # vertical lines
    pg.draw.line(MainDisplay, black, (Width / 3, 0), (Width / 3, Height), 6)
    pg.draw.line(MainDisplay, black, (Width / 3 * 2, 0), (Width / 3 * 2, Height), 6)
    pg.draw.line(MainDisplay, black, (0, 0), (0, Height), 6)
    pg.draw.line(MainDisplay, black, (Width, 0), (Width, Height), 6)

    # horizontal lines
    pg.draw.line(MainDisplay, black, (0, 0), (Width, 0), 6)
    pg.draw.line(MainDisplay, black, (0, Height / 3), (Width, Height / 3), 6)
    pg.draw.line(MainDisplay, black, (0, Height / 3 * 2), (Width, Height / 3 * 2), 6)
    pg.draw.line(MainDisplay, black, (0, Height), (Width, Height), 6)

    pg.display.update()
    DrawAdditionalInfo()


def DrawAdditionalInfo():
    global Draw, SecondPlayerSymbol, WhoseTurn, StartingPlayerSymbol

    if TheWinner is None:
        NewMessage = "It's your turn Mr. " + str(WhoseTurn)

    else:
        NewMessage = "You won, Mr. " + str(TheWinner)

    if Draw:
        NewMessage = "It's a DRAW, try again! "

#GUI SCORE ETC.

    Font = pg.font.Font(None, 25)
    MessageResult = Font.render(NewMessage, True, white)
    Points = name1 + " [ " + StartingPlayerSymbol +" ] : " + str(FirstPlayerPoints)  + " | " + str(SecondPlayerPoints) + " : " + "[ " + SecondPlayerSymbol+" ] " + name2
    MessagePoints = Font.render(Points, True, black)

    MessageResultSurround = MessageResult.get_rect(center=(Width / 2, 480 - 40))
    MessagePointsSurround = MessagePoints.get_rect(center=(Width / 2, 580 - 50))

    MainDisplay.fill((128, 0, 0), (0, 400, 400, 90))
    MainDisplay.blit(MessageResult, MessageResultSurround)
    MainDisplay.blit(MessagePoints, MessagePointsSurround)

    pg.display.update()


def WhetherWin():
    global Board, TheWinner, Draw

    # check if there is a horizontal winning line (czy ktos wygral w poziomie)

    for Row in range(0, 3):
        if ((Board[Row][0]) == Board[Row][1] == Board[Row][2]) and (Board[Row][0] is not None):
            TheWinner = Board[Row][0]
            pg.draw.line(MainDisplay, (128, 0, 0), (0, (Row + 1) * Height / 3 - Height / 6),
                         (Width, (Row + 1) * Height / 3 - Height / 6), 4)
            break

    # check if there is a vertical winning line (czy ktoś wygrał w pionie)

    for Column in range(0, 3):
        if ((Board[0][Column] == Board[1][Column] == Board[2][Column]) and (Board[0][Column] is not None)):
            TheWinner = Board[0][Column]
            pg.draw.line(MainDisplay, (128, 0, 0), (Width / 3 * (Column + 1) - Width / 6, 0),
                         (Width / 3 * (Column + 1) - Width / 6, Height), 4)
            break

    # check if there is a diagonal winning line (czy ktoś wygrał w ukosie)
    if ((Board[0][0] == Board[1][1] == Board[2][2]) and (Board[0][0]) is not None):
        TheWinner = Board[0][0]
        pg.draw.line(MainDisplay, (128, 0, 0), (0, 0), (Width, Height), 5)

    if ((Board[0][2] == Board[1][1] == Board[2][0]) and (Board[0][2]) is not None):
        TheWinner = Board[0][2]
        pg.draw.line(MainDisplay, (128, 0, 0), (Width, 0), (0, Height), 5)

    # there is no winner
    if (all([all(Row) for Row in Board]) and TheWinner is None):
        Draw = True

    # DRAW DRAW
    DrawAdditionalInfo()


def DrawSymbol(Row, Column):
    global Board, WhoseTurn, XPos, YPos
    # position X of new symbol image
    if Row == 1:
        YPos = 30

    elif Row == 2:
        YPos = Width / 3 + 30

    elif Row == 3:
        YPos = Width / 3 * 2 + 30
    # position Y of new symbol image
    if Column == 1:
        XPos = 30

    elif Column == 2:
        XPos = Height / 3 + 30

    elif Column == 3:
        XPos = Height / 3 * 2 + 30

    Board[Row - 1][Column - 1] = WhoseTurn

    if (WhoseTurn == 'X'):
        MainDisplay.blit(ImageOfX, (XPos, YPos))
        WhoseTurn = 'O'
    elif (WhoseTurn == 'O'):
        MainDisplay.blit(ImageOfO, (XPos, YPos))
        WhoseTurn = 'X'

    DrawAdditionalInfo()
    pg.display.update()


def CheckField():
    # mouse position
    global Column
    global Row
    pos = pg.mouse.get_pos()

    # horizontal X
    if (pos[0] < Width / 3):
        Column = 1
    elif (pos[0] < Width / 3 * 2):
        Column = 2
    elif (pos[0] < Width):
        Column = 3
    else:
        Column = None

    # vertical Y
    if (pos[1] < Height / 3):
        Row = 1
    elif (pos[1] < Height / 3 * 2):
        Row = 2
    elif (pos[1] < Height):
        Row = 3

    else:
        Row = None

    print(WhoseTurn + " na pole: " + str(Row), str(Column))
    if Row is not None and Column is not None and Board[Row - 1][Column - 1] is None:
        DrawSymbol(Row, Column)
        WhetherWin()


CreateBoard()


def GameRestart():
    global Board, WhoseTurn, TheWinner, Draw, SecondPlayerPoints, FirstPlayerPoints, name1, name2, StartingPlayerSymbol, SecondPlayerSymbol
    time.sleep(3)
    WhoseTurn = 'X'
    Draw = False
    if TheWinner == StartingPlayerSymbol:
        FirstPlayerPoints += 1

    elif TheWinner == SecondPlayerSymbol:
        SecondPlayerPoints +=1

    TheWinner = None
    Board = [[None] * 3, [None] * 3, [None] * 3]
    MainDisplay.fill(white)
    CreateBoard()
    pg.display.update()


while (True):
    for Event in pg.event.get():
        pg.display.update()
        if Event.type == pg.QUIT:
            print('Poprawne wyjscie z gry.')
            pg.quit()
            sys.exit()

        elif Event.type == pg.MOUSEBUTTONDOWN:
            CheckField()
            if (TheWinner or Draw):
                text = ''
                now = datetime.now()
                realtimeformat = now.strftime("%d/%m/%Y %H:%M:%S")
                if (TheWinner):
                    print("KONIEC ROZGRYWKI")
                    text = '''<br> ######################################### <br> <br> Data:''' +realtimeformat + "<br>" + name1 +\
                           " [" + StartingPlayerSymbol + "] vs " + name2 + " [" + SecondPlayerSymbol +"] " +  '''
                    <br> Zwyciezca: ''' + str(TheWinner) + '''<br> Zaczynajacy: ''' +\
                           StartingPlayerSymbol + ''' <br> Kolor planszy: ''' + color + '''
                                   
                                     <br> <br>
                                     #########################################
                                     '''
                    if StartingPlayerSymbol == 'O':
                        StartingPlayerSymbol = 'X'
                    else:
                        StartingPlayerSymbol = "O"
                if (Draw):
                    print("KONIEC ROZGRYWKI")
                    text = '''<br> ######################################### <br> <br> Data: to''' + realtimeformat + "<br>" + name1 + \
                           " [" + StartingPlayerSymbol + "] vs " + name2 + " [" + SecondPlayerSymbol + "] " + '''
                                        <br> Zwyciezca: brak - REMIS <br> Zaczynajacy: ''' + \
                           StartingPlayerSymbol + ''' <br> Kolor planszy: ''' + color + '''

                                                         <br> <br>
                                                         #########################################
                                                         '''
                    if StartingPlayerSymbol == 'O':
                        StartingPlayerSymbol = 'X'
                    else:
                        StartingPlayerSymbol = "O"
                file = open("C:/TicTacToe/Wyniki.html", "a")
                file.write(text)
                file.close()
                GameRestart()
                pg.display.update()

TimeClock.tick(FPS)
DrawAdditionalInfo()
