import turtle 
import time
import winsound

Score = 0


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Game")
wn.bgpic("wp3284832.gif")
wn.tracer()

turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("boom.gif")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")                                                                                                                                                            
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
pen.goto(0, 240)
pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
pen.goto(0, 220)
pen.write("Score 15 to win", align="center", font=("Courier", 10, "normal"))

for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bullet.goto(500,500)

bulletspeed = 40

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("enemy.gif")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,270)


enemyspeed = 6


bulletstate = "ready"

def move_left():
    player.speed = - 10


def move_right():
    player.speed = 10



def move_player():
     x = player.xcor()
     x += player.speed
     if x < - 280:
        x = - 280
     if x > 274:
         x = 274
     player.setx(x)




def fire_bullet():
    global bulletstate

    if bulletstate == "ready":
        bulletstate = "fire"
        bullet.showturtle()
        y = player.ycor() + 10
        x = player.xcor()
        bullet.setposition(x , y)
        winsound.PlaySound("cartoon016.wav", winsound.SND_ASYNC)


wn.listen()
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_left, "Left")
wn.onkeypress(fire_bullet, "space")
# Alt to pause

while True: 

    wn.update()

    border_pen.color("white")   

    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    move_player()


    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed*= -1
        enemy.sety(y)

    if enemy.xcor() < - 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed*= -1
        enemy.sety(y)

    if bullet.ycor() > 270:
        bullet.hideturtle()
        bulletstate = "ready"

    if bullet.distance(enemy) < 25:
        winsound.PlaySound("cartoon007.wav", winsound.SND_ASYNC)
        Score +=1
        pen.clear()
        pen.goto(0, 260)
        pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal")) 
        pen.goto(0, 240)
        pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Score 15 to win", align="center", font=("Courier", 10, "normal"))
        bullet.hideturtle()
    

    if enemy.ycor() < - 266:                                                                                                                                                            
        enemy.hideturtle()
        bullet.hideturtle()
        player.hideturtle()
        pen.clear()
        pen.goto(0, 260)
        pen.color("red")
        pen.write("You Lose".format("You lose"), align="center", font=("Courier", 24, "normal")) 
        time.sleep(8)
        exit()


    if Score == 15:
        border_pen.color("green") 
        enemy.shape("boom.gif")                                                                                                                                                           
        winsound.PlaySound("battle003.wav", winsound.SND_ASYNC)
        bullet.hideturtle()
        player.hideturtle()
        pen.clear()
        pen.goto(0, 260)
        pen.color("green")
        pen.write("You Won!".format("You Won!"), align="center", font=("Courier", 24, "normal")) 
        time.sleep(3)
        exit()

wn.mainloop()