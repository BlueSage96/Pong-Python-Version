#https://www.youtube.com/watch?v=XGf2GcyHPhc
#beginner version - not using OOP for this
#https://www.dropbox.com/sh/23xxa0zmm8ft93c/AABhYEvuBYv7ots2io2QPdgla?dl=0&preview=pong+turtle.py

#sound
#https://www.youtube.com/watch?v=YZknoOWCaj4&feature=youtu.be
import turtle
import os
import easygui

win = turtle.Screen()
win.title("Pong by Brittany Price")
win.bgcolor("black")
win.setup(width=800, height=600)

#stops window from  - we manual update it - makes game run faster
win.tracer(0)

#Score
scoreA = 0
scoreB = 0

#line1
line1 = turtle.Turtle()
line1.shape("square")
line1.color("white")
line1.shapesize(stretch_wid=30,stretch_len=0.1)
line1.penup()
line1.goto(0, 0)

#line2
line2 = turtle.Turtle()
line2.shape("square")
line2.color("white")
line2.shapesize(stretch_wid=0.1,stretch_len=40)
line2.penup()
line2.goto(0, 255)

#circle in the center - needed to move goto above pensize & drawing shape
#had pensize after drawing the circle:
#https://www.youtube.com/watch?v=XevEnR2Q1XM
mid_circle = turtle.Turtle()
mid_circle.color("white")
mid_circle.goto(0,-100)
mid_circle.pensize(4)
mid_circle.circle(radius=90)

mid_circle.hideturtle()
mid_circle.penup()

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("blue")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-380, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("red")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(370, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)#0,0 - middle

#ball speed
ball.dx = 3#moves by blank pixels
ball.dy = -3

#Pen
pen = turtle.Turtle() #turtle -> module name Turtle -> class name
pen.speed(0)
pen.color("white")
pen.penup() #keeps text from moving
pen.hideturtle()
pen.goto(0, 265)
pen.write("Player 1: 0    Player 2: 0", align="center", font=("Courier", 20, "normal"))

# Functions
def paddleAUp():
    if paddleA.ycor() <= 170:  # If paddle is below the top (y = 250) - move up 40 pixels
        paddleA.sety(paddleA.ycor() + 40)

def paddleADown():
    if paddleA.ycor() >= -200:
        paddleA.sety(paddleA.ycor()-40)

def paddleBUp():
    if paddleB.ycor() <= 170:  # If paddle is below the top (y = ) - move up 40 pixels
        paddleB.sety(paddleB.ycor()+40)

def paddleBDown():
    if paddleB.ycor() >= -200:
        paddleB.sety(paddleB.ycor()-40)

# Keyboard bindings
win.listen()
win.onkeypress(paddleAUp, "w")
win.onkeypress(paddleADown, "s")
win.onkeypress(paddleBUp, "Up")
win.onkeypress(paddleBDown, "Down")

game_over = False
#main game loop
#everytime loop runs the screen updates
while not game_over:
    win.update()

    #Move the ball - starts at (0,0)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking

    #top
    if ball.ycor() > 245:
        ball.sety(245)
        ball.dy *= -1 #reverses direction

    #bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverses direction

    #right - going past the paddle
    if ball.xcor() > 380:
        ball.goto(0,0) #put ball back at the center
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(scoreA, scoreB), align="center", font=("Courier", 20, "normal"))

    #left - going past the paddle
    if ball.xcor() < -390:
        ball.goto(0,0) #put ball back at the center
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(scoreA, scoreB), align="center", font=("Courier", 20, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 350 and ball.xcor() < 370)and (ball.ycor() < paddleB.ycor() + 60 and ball.ycor() > paddleB.ycor() - 60):
        ball.setx(350)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -360 and ball.xcor() > -380)and (ball.ycor() < paddleA.ycor() + 60 and ball.ycor() > paddleA.ycor() - 60):
        ball.setx(-360)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

        # Stop if player reaches 10
    if scoreA == 10 or scoreB == 10:
            game_over = True