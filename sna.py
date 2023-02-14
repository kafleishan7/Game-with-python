import turtle as t
import os
import time as ti
import random

delay=0.1
score=0
highscore=0

window=t.Screen()
window.title("Snake_Gmae")
window.screensize(720,720)
window.bgcolor('sky blue')
window.tracer(0)

window.cv._rootwindow.resizable(False, False)

head=t.Turtle()
head.shape('circle')
head.color('red')
head.speed(0)
head.penup()
head.goto(0,0)
head_x=.3
head_y=.3

# head.direction = "Stop"



# eat_thing=t.Turtle()
# eat_thing = t.Turtle()
# colorss = random.choice(['red', 'green', 'black'])
# shapes = random.choice(['square', 'triangle', 'circle'])
# eat_thing.shape(shapes)
# eat_thing.color(colorss)
# eat_thing.penup()




pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))
 

pen2_top=t.Turtle()
pen2_top.speed(0)
pen2_top.shape('square')
pen2_top.shapesize(stretch_len=90,stretch_wid=.2)
pen2_top.color('black')
pen2_top.penup()
# pe_topn2.hideturtle()
pen2_top.goto(-475, 310)

pen3_down=t.Turtle()
pen3_down.speed(0)
pen3_down.shape('square')
pen3_down.shapesize(stretch_len=90,stretch_wid=1)
pen3_down.color('black')
pen3_down.penup()
# pe_downn2.hideturtle()
pen3_down.goto(-475, -310)

pen4_left=t.Turtle()
pen4_left.speed(0)
pen4_left.shape('square')
pen4_left.shapesize(stretch_len=.2,stretch_wid=90)
pen4_left.color('black')
pen4_left.penup()
# pe_leftn4n2.hideturtle()
pen4_left.goto(-370,310)

pen5_right=t.Turtle()
pen5_right.speed(0)
pen5_right.shape('square')
pen5_right.shapesize(stretch_len=.2,stretch_wid=90)
pen5_right.color('black')
pen5_right.penup()
# p5_rightn4n2.hideturtle()
pen5_right.goto(365,310)

# #Key direction
# def goUp():
#     if head.direction !="down":
#         head.direction= "up"
# def goDown():
#     if head.direction !="up":
#         head.direction="down"

# def goLeft():
#     if head.directiom !="right":
#         head.direction="left"


# def goRight():
#     if head.directiom !="left":
#         head.direction="right"

# def move():
#     if head.direction=="up":
#         y=head.ycor()
#         head.sety(y+20)
    
#     if head.direction=="down":
#         y=head.ycor()
#         head.sety(y-20)

#     if head.direction=="left":
#         x=head.xcor()
#         head.setx(x-20)
    
#     if head.direction=="right":
#         x=head.xcor()
#         head.setx(x+20)

    
# window.listen()
# window.onkeypress(goUp, "w")
# window.onkeypress(goDown, "s")
# window.onkeypress(goLeft, "a")
# window.onkeypress(goRight, "d")
# window.onkeypress(goUp, "Up")
# window.onkeypress(goDown, "Down")
# window.onkeypress(goLeft, "Left")
# window.onkeypress(goRight, "Right")





while True:
    window.update()
    # if head.xcor() > 
    head.setx(head.ycor() + head_x)
    head.sety(head.ycor() + head_y)

    if(head.xcor()>pen5_right.xcor() or head.ycor()> pen2_top.ycor()):
        head.left(90)
        t.forward(400)
        # head.goto(0,0)


    # move()