import pygame
from numpy import *
from random import randint,sample
import time
i = 0
j = 0
pygame.init()
width=800
height=600
black=(0,0,0)
sel_box=(225,228,255)
start = pygame.image.load("start1.png")
abt = pygame.image.load("about.png")
quit = pygame.image.load("quit.png")
x1= pygame.image.load("X.png")
o1= pygame.image.load("O.png")
gamedisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic Tac Toe")
clock=pygame.time.Clock()
def about():
    a=1
    while a:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        print(mouse)
        gamedisplay.fill((255,255,255))
        message_display("Created by Tanish",75,(width/2),(height*0.5),black)
        pygame.draw.rect(gamedisplay, (255,0,0),(35,10,100,50))
        message_display("Back",30,85,35,(0,0,0))
        if mouse[0]>35 and mouse[1]>10  and mouse[0]<135 and mouse[1]<60:
            pygame.draw.rect(gamedisplay, (100,0,0),(35,10,100,50))
            message_display("Back",30,85,35,(0,0,0))
            click=pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a=False
        clock.tick(10)
    pygame.display.update()
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        print(mouse)
        gamedisplay.fill((255,255,255))
        message_display("Tic Tac Toe",70,(width/2),(height*0.4),black)
        gamedisplay.blit(start, (100,425))
        #pygame.display.update()
        gamedisplay.blit(abt, (350, 425))
        # pygame.display.update()
        gamedisplay.blit(quit, (600, 425))

        if mouse[0]>100 and mouse[1]>425  and mouse[0]<200 and mouse[1]<475:
            pygame.draw.rect(gamedisplay, (0,100,0),(100,425,100,50))
            message_display("Start",30,150,450,(0,0,0))
            click=pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameloop()
        if mouse[0]>600 and mouse[1]>425  and mouse[0]<700 and mouse[1]<475:
            pygame.draw.rect(gamedisplay, (100,0,0),(600,425,100,50))
            message_display("QUIT",30,650,450,(0,0,0))
            click=pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        if mouse[0]>((width/2)-50) and mouse[1]>425  and mouse[0]<((width/2)+50) and mouse[1]<475:
            pygame.draw.rect(gamedisplay, (0,0,100),((width/2)-50,425,100,50))
            message_display("About",30,width/2,450,(0,0,0))
            click=pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                about()
        pygame.display.update()
        clock.tick(15)
def text_objects(text, font,color):
    textSurface = font.render(text, True,color)
    return textSurface, textSurface.get_rect()

def message_display(text,size,x,y,color):
    largeText = pygame.font.SysFont('comicsansms',size)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = ((x,y))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
def ai_move(ex,big,big1,k,j):       #  TODO bug fixing
    def check(board):
        winner = 0
        for i in range(3):
            if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0):
                winner=1
            if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0):
                winner=1
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0):
            winner=1
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0):
            winner=1
        return winner
    win=0
    for i in range(2,0,-1):
        for r in range(3):
            for c in range(3):
                if ex[r][c] == 0:
                    ex[r][c] = i
                    win = check(ex)
                    if win:
                        ex[r][c] = 2
                        return ex
                    else:
                        ex[r][c] = 0
    if win==0:
        again=True
        while again==True :
            if big[k]==1:
                if ex[0][0]== 0:
                    ex[0][0] =2

                    if k<4:
                        k+=1
                    return ex
                else:
                    again = True
                    if k<4:
                        k+=1
                    #return ex
            if big[k] == 2:
                if ex[0][2]== 0:
                    ex[0][2] = 2
                    if k<4:
                        k+=1
                    return ex
                else:
                    again=True
                    if k < 4:
                        k += 1
                    #return ex
            if big[k] == 3:
                if ex[2][0] == 0:
                    ex[2][0] = 2
                    if k<4:
                        k+=1
                    return ex
                else:
                    again=True
                    if k < 4:
                        k += 1
                    #return ex
            if big[k] == 4:
                if ex[2][2] == 0:
                    ex[2][2] = 2
                    if k<4:
                        k+=1
                    return ex
                else:
                    again = True
                    if k < 4:
                        k += 1
                    #return ex
            if big[k] == 5:
                if ex[1][1] == 0:
                    ex[1][1] = 2
                    if k<4:
                        k+=1
                    return ex
                else:
                    again = True
                    if k < 4:
                        k += 1
                    #return ex
            if k==4:
                again=False

        if k==4:
            again=True
            while again:
                if big1[j] == 1:
                    if ex[0][1] == 0:
                        ex[0][1] = 2
                        if j < 3:
                            j += 1
                        return ex
                    else:
                        again = True
                        if j < 3:
                            j += 1
                        #return ex
                if big1[j] == 2:
                    if ex[1][0] == 0:
                        ex[1][0] = 2
                        if j < 3:
                            j += 1
                        return ex
                    else:
                        again = True
                        if j < 3:
                            j += 1
                        #return ex
                if big1[j] == 3:
                    if ex[2][1] == 0:
                        ex[2][1] = 2
                        if j < 3:
                            j += 1
                        return ex
                    else:
                        again = True
                        if j < 3:
                            j += 1
                        #return ex
                if big1[j] == 4:
                    if ex[1][2] == 0:
                        ex[1][2] = 2
                        if j < 3:
                            j += 1
                        return ex
                    else:
                        again = True
                        if j < 3:
                            j += 1
                    #return ex


def check_winner(board):
    winner=0
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] !=0):
            winner = board[i][0]
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] !=0):
            winner = board[0][i]
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] !=0):
        winner = board[0][0]
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] !=0):
        winner = board[0][2]
    #if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == board[0][1] and board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == board[2][0] and board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[0][0] !=0):
    #   winner = '0'
    if(winner==1):
        time.sleep(0.5)
        gamedisplay.fill((255, 255, 255))
        message_display("You Win", 70, (width / 2), (height * 0.4), black)
        pygame.display.update()
        time.sleep(2)
        gameloop()
    elif(winner==2):
        time.sleep(0.5)
        gamedisplay.fill((255, 255, 255))
        message_display("AI Wins", 70, (width / 2), (height * 0.4), black)
        pygame.display.update()
        time.sleep(2)
        gameloop()



def gameloop():
    board = zeros(3 * 3, int)
    # for i in range(9):
    # board[i] = "_"
    board = board.reshape(3, 3)
    print(board)
    trn=1
    intro = True
    big = sample(range(1, 6), 5)
    big1 = sample(range(1, 5), 4)

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        print(mouse)
        gamedisplay.fill((255, 255, 255))
        pygame.draw.rect(gamedisplay,black, ((width/2)+50,140, 10, 320))
        pygame.draw.rect(gamedisplay, black, ((width/2)-60, 140, 10, 320))
        pygame.draw.rect(gamedisplay, black, (240, (height/2)-60, 320, 10))
        pygame.draw.rect(gamedisplay, black, (240, (height/2)+50, 320, 10))
        #message_display("You are X", 30, 85, 35, (0, 0, 0))
        check_winner(board)
        if trn%2==1:
            if board[0][0]==0:
                if mouse[0] > 250 and mouse[1] > 150 and mouse[0] < 350 and mouse[1] < 250:
                    pygame.draw.rect(gamedisplay, sel_box, (245, 145, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[0][0]=1
                        trn+=1
            if board[1][0] == 0:
                if mouse[0] > 250 and mouse[1] > 250 and mouse[0] < 350 and mouse[1] < 350:
                    pygame.draw.rect(gamedisplay, sel_box, (245, 255, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[1][0]=1
                        trn += 1
            if board[2][0] == 0:
                if mouse[0] > 250 and mouse[1] > 360 and mouse[0] < 350 and mouse[1] < 460:
                    pygame.draw.rect(gamedisplay, sel_box, (245, 365, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[2][0]=1
                        trn += 1
            if board[0][1] == 0:
                if mouse[0] > 350 and mouse[1] > 150 and mouse[0] < 450 and mouse[1] < 250:
                    pygame.draw.rect(gamedisplay, sel_box, (355, 145, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[0][1] = 1
                        trn += 1
            if board[1][1] == 0:
                if mouse[0] > 350 and mouse[1] > 250 and mouse[0] < 450 and mouse[1] < 350:
                    pygame.draw.rect(gamedisplay, sel_box, (355, 255, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[1][1] = 1
                        trn += 1
            if board[2][1] == 0:
                if mouse[0] > 350 and mouse[1] > 360 and mouse[0] < 450 and mouse[1] < 460:
                    pygame.draw.rect(gamedisplay, sel_box, (355, 365, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[2][1] = 1
                        trn += 1
            if board[0][2] == 0:
                if mouse[0] > 455 and mouse[1] > 150 and mouse[0] < 550 and mouse[1] < 250:
                    pygame.draw.rect(gamedisplay, sel_box, (465, 145, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[0][2] = 1
                        trn += 1
            if board[1][2] == 0:
                if mouse[0] > 455 and mouse[1] > 250 and mouse[0] < 550 and mouse[1] < 350:
                    pygame.draw.rect(gamedisplay, sel_box, (465, 255, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[1][2] = 1
                        trn += 1
            if board[2][2] == 0:
                if mouse[0] > 455 and mouse[1] > 360 and mouse[0] < 550 and mouse[1] < 460:
                    pygame.draw.rect(gamedisplay, sel_box, (465, 365, 90, 90))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board[2][2] = 1
                        trn += 1
        elif trn%2==0 :
            trn += 1
            check_winner(board)
            board=ai_move(board,big,big1,i,j)


        if board[0][0]==1:
            gamedisplay.blit(x1, (245, 145))
        if board[1][0]==1:
            gamedisplay.blit(x1, (245, 255))
        if board[2][0]==1:
            gamedisplay.blit(x1, (245, 365))
        if board[0][1]==1:
            gamedisplay.blit(x1, (355, 145))
        if board[1][1]==1:
            gamedisplay.blit(x1, (355, 255))
        if board[2][1]==1:
            gamedisplay.blit(x1, (355, 365))
        if board[0][2]==1:
            gamedisplay.blit(x1, (465, 145))
        if board[1][2]==1:
            gamedisplay.blit(x1, (465, 255))
        if board[2][2]==1:
            gamedisplay.blit(x1, (465, 365))
        if board[0][0]==2:
            gamedisplay.blit(o1, (245, 145))
        if board[1][0]==2:
            gamedisplay.blit(o1, (245, 255))
        if board[2][0]==2:
            gamedisplay.blit(o1, (245, 365))
        if board[0][1]==2:
            gamedisplay.blit(o1, (355, 145))
        if board[1][1]==2:
            gamedisplay.blit(o1, (355, 255))
        if board[2][1]==2:
            gamedisplay.blit(o1, (355, 365))
        if board[0][2]==2:
            gamedisplay.blit(o1, (465, 145))
        if board[1][2]==2:
            gamedisplay.blit(o1, (465, 255))
        if board[2][2]==2:
            gamedisplay.blit(o1, (465, 365))
        pygame.display.update()
        clock.tick(60)
        if trn == 10:
            time.sleep(0.5)
            gamedisplay.fill((255, 255, 255))
            message_display("Draw", 70, (width / 2), (height * 0.4), black)
            pygame.display.update()
            time.sleep(2)
            gameloop()

game_intro()