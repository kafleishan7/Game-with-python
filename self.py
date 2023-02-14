# https://youtu.be/cxm5bCCa9OA

import turtle as t
import os

playerAscore=0
playerBscore=0


# creating window screen

window=t.Screen()
window.title("THis is my first game")
window.bgcolor('light blue')
window.setup(width=800, height=600)
window.tracer(0)

#creating left paddle variable
leftpadle=t.Turtle()
leftpadle.speed(0)
leftpadle.shape("square")
leftpadle.color('red')
leftpadle.shapesize(stretch_wid=7,stretch_len=2)
leftpadle.penup()
leftpadle.goto(-350,0)

#Creating the right paddlevariable

rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.color('red')
rightpaddle.shape('square')
rightpaddle.shapesize(stretch_len=2, stretch_wid=7)
rightpaddle.penup()
rightpaddle.goto(350,0)


vkundo=t.Turtle()
vkundo.shape('circle')
vkundo.speed(0)
vkundo.penup()
vkundo.color('blue')
vkundo.goto(0,0)

ball_dx = .3   # Setting up the pixels for the ball movement.
ball_dy = .3


#Score update

pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}      Player B: {} ".format(playerAscore, playerBscore), align="center", font=('Monaco', 24, "normal"))

pen2=t.Turtle()
pen2.speed(0)
pen2.color("Green")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)
pen2.write("PRESS SPACE TO START THE GAME ...", align="center", font=('Tahoma', 24, "normal"))


def leftpaddleup():
        y=leftpadle.ycor()
        y=y+15
        leftpadle.sety(y)

def leftpaddledown():
        y=leftpadle.ycor()
        y=y-15
        leftpadle.sety(y)


    # codefor move rightpadhle
def rightpaddleup():
        y=rightpaddle.ycor()
        y=y+15
        rightpaddle.sety(y)

def rightpaddledown():
        y=rightpaddle.ycor()
        y=y-15
        rightpaddle.sety(y)


def spacebtnwork():
    global playerAscore
    global playerBscore

# code for move leftpaddle
    ballxdirection=.5
    ballydirection=.5

    # to add key move
    window.onkeypress(leftpaddleup,'w')
    window.onkeypress(leftpaddledown,'s')
    window.onkeypress(rightpaddleup,'Up')
    window.onkeypress(rightpaddledown,'Down')



    while True:
            window.update()
            #Moving ball
            vkundo.setx(vkundo.xcor()+ballxdirection)
            vkundo.sety(vkundo.ycor()+ballydirection)


            if vkundo.ycor()> 290:
                vkundo.sety(290)
                ballydirection=ballydirection * -1

            if vkundo.ycor()<-290:
                vkundo.sety(-290)
                ballydirection=ballydirection*-1

            if vkundo.xcor()> 390:
                # vkundo.goto(0,0)
                ballxdirection=ballxdirection*-1
                playerAscore=playerAscore+1
                pen.clear()
                pen.write("Player A: {}      Player B: {} ".format(
                playerAscore, playerBscore), align="center", font=('Monaco', 24, "normal"))
                os.system("afplay wallhit.wav&")
            #Left width paddle border

            if vkundo.xcor() <-390:
                # vkundo.goto(0,0)
                ballxdirection=ballxdirection*-1
                playerBscore=playerBscore+1
                pen.clear()
                pen.write("Player A: {}      Player B: {} ".format(
                playerAscore, playerBscore), align="center", font=('Monaco', 24, "normal"))
                os.system("afplay wallhit.wav&")


            if (vkundo.xcor() > 340) and (vkundo.xcor() < 350) and (vkundo.ycor() < rightpaddle.ycor()+100 and vkundo.ycor() > rightpaddle.ycor() - 100):
                vkundo.setx( 340)
                ballxdirection=ballxdirection*-1
                os.system("afplay paddle.wav&")

            if (vkundo.xcor() < -340) and (vkundo.xcor() > -350) and (vkundo.ycor() < leftpadle.ycor() +100 and vkundo.xcor() > leftpadle.xcor() - 100):
                vkundo.setx(-340)
                ballxdirection=ballxdirection*-1
                os.system("afplay paddle.wav&")

            print(vkundo.pos())

loop=True
while loop==True:

    input=(input(""))
    if(input!=""):
        loop=True
    else:
        loop=False
        spacebtnwork()









    # import time as ti
    # ti.sleep(5)