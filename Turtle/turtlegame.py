import turtle
import random
import time
from playsound import playsound
# colors lists
colors = ['red', 'yellow', 'green', 'white']
# setting up the window screen

playsound('start.aiff', False)
win = turtle.Screen()
win.title('Turtle :-Suman')
win.setup(width=600, height=600)
win.bgpic('startingpic.gif')
win.bgcolor('lightgreen')
# setting up the border of game:
border = turtle.Turtle()
border.penup()
border.turtlesize(2)
border.color('green', 'red')
border.setposition(-280, -280)
border.pendown()
border.pensize(3)
for i in range(4, 0, -1):
    border.forward(552)
    border.left(90)
border.hideturtle()
border.penup()
border.color('red')
border.setposition(-210, 0)
border.write("Turtle Game: \nSuman Raj Khanal",
             font=('Courier', 30, 'normal'))
time.sleep(2)
border.undo()
# border 2
border2 = turtle.Turtle()
border2.penup()
border2.turtlesize(3)
border2.color('green', 'orange')
border2.setposition(-280, -280)
border2.pendown()
border2.pensize(3)
for i in range(4, 0, -1):
    border2.forward(552)
    border2.left(90)
border2.hideturtle()
border2.penup()
border2.color('red')
border2.setposition(0, 0)
border2.write('Help: \n1. Speed up "Up" Key\n2. Go left "Left" key\n3. Go right "Right" key', move=True, align='center',
              font=('Courier', 25, 'normal'))
time.sleep(4)
border2.undo()

# score for the game:
score = 0
high_score = 0

# food for turtle
food = turtle.Turtle()
food.color(random.choice(colors))
food.shape('circle')
food.speed(0)
food.penup()
food.turtlesize(1)
food.setposition(random.randint(-270, 270), random.randint(-270, 270))
food.right(random.randint(0, 360))
# game player
player = turtle.Turtle()
player.color(random.choice(colors))
player.turtlesize(2)
player.shape('turtle')
player.speed(0)
player.penup()
player.setposition(0, 0)

# setting up the speed:
speed = 0.1

# function for turtle control


def moveleft():
    player.left(45)


def moveright():
    player.right(45)


def movespeed():
    global speed
    speed += 0.1


# setting up the control of the turtle:
turtle.listen()
turtle.onkeypress(moveleft, 'Left')
turtle.onkeypress(moveright, 'Right')
turtle.onkeypress(movespeed, 'Up')

# main process on game i.e main loop
while True:
    player.forward(speed)
    speed += 0.001
    food.forward(1)
    # distance btn food and turtle
    if player.distance(food) < 25:
        playsound('ring.wav', False)
        food.setposition(random.randint(-270, 270), random.randint(-270, 270))
        food.right(random.randint(0, 360))
        food.color(random.choice(colors))
        score += 10
        if score > high_score:
            high_score = score
        border.penup()
        border.hideturtle()
        border.setposition(-190, 220)

        border.clear()
        border.write(f"Score:{score} HighScore: {high_score}",
                     font=('Courier', 25, 'normal'))
    # player return on touching border
    if player.xcor() > 265 or player.xcor() < -265:

        score = 0
        border.undo()
        border.write(f"Score:{score} HighScore: {high_score}",
                     font=('Courier', 25, 'normal'))
        playsound('sound.wav', False)
        player.setposition(0, 0)
        speed = 0.1
    if player.ycor() > 265 or player.ycor() < -265:

        border.undo()
        score = 0
        border.write(f"Score:{score} HighScore: {high_score}",
                     font=('Courier', 25, 'normal'))
        playsound('sound.wav', False)
        player.setposition(0, 0)
        speed = 0.1
    # food returns back touching borders
    if food.xcor() > 270 or food.xcor() < -270:
        food.right(180)
    if food.ycor() > 270 or food.ycor() < -270:
        food.left(180)

win.mainloop()
