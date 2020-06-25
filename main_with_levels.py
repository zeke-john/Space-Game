import turtle 
import time
import winsound

Score = 0

level = 1

wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("wp3284832.gif")
wn.title("Space Game")
wn.tracer()


turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("boom.gif")
turtle.register_shape("2nd_enemy.gif")
turtle.register_shape("3nd_enemy.gif")



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

bulletspeed = 50

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

    if bullet.ycor() > 265:
        bullet.hideturtle()
        bulletstate = "ready"

    if bullet.distance(enemy) < 27.5:
        winsound.PlaySound("cartoon007.wav", winsound.SND_ASYNC)
        Score +=1
        pen.clear()
        pen.goto(0, 260)
        pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal")) 
        pen.goto(0, 240)
        pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
        bullet.hideturtle()

    if enemy.ycor() < - 266:                                                                                                                                                            
        enemy.hideturtle()
        bullet.hideturtle()
        player.hideturtle()
        pen.clear()
        pen.goto(0, 260)
        pen.color("red")
        pen.write("You Lose".format("You lose"), align="center", font=("Courier", 24, "normal")) 
        time.sleep(7)
        level = 1
        Score = 0
        enemy.showturtle()
        bullet.showturtle()
        player.showturtle()
        player.goto(0,-250)
        enemy.goto(0, 250)
        bullet.goto(500, 500)
        enemy.shape("enemy.gif")
        pen.clear()
        pen.color("white")
        pen.goto(0, 260)
        pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal")) 
        pen.goto(0, 240)
        pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Score 10 to pass level 1", align="center", font=("Courier", 10, "normal"))


    if Score == 10 and level == 1:
        enemy.shape("boom.gif")                                                                                                                                                           
        winsound.PlaySound("battle003.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.goto(0, 260)
        pen.write("Level 1 completed".format("level 1 completed"), align="center", font=("Courier", 24, "normal")) 
        time.sleep(3)
        pen.clear()
        enemy.goto(-200,250)
        level +=1
        Score = 0
    
    if Score == 15 and level == 2:
        enemy.shape("boom.gif")                                                                                                                                                           
        winsound.PlaySound("battle003.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.goto(0, 250)
        pen.write("Level 2 completed".format("level 2 completed"), align="center", font=("Courier", 24, "normal")) 
        time.sleep(3)
        pen.clear()
        enemy.goto(-200,260)
        level +=1
        Score = 0

    if Score == 20 and level == 3:
        pen.goto(0, 250)
        enemy.shape("boom.gif")                                                                                                                                                           
        winsound.PlaySound("battle003.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.goto(0, 260)
        pen.color("green")
        enemy.shape("boom.gif") 
        pen.write("You Won!".format("You Won!"), align="center", font=("Courier", 24, "normal"))
        enemy.hideturtle()
        bullet.hideturtle()
        player.hideturtle()
        level +=1 
        time.sleep(7)
        level = 1
        Score = 0
        enemy.showturtle()
        bullet.showturtle()
        player.showturtle()
        player.goto(0,-250)
        enemy.goto(0, 250)
        bullet.goto(500, 500)
        enemy.shape("enemy.gif")
        pen.clear()
        pen.color("white")
        pen.goto(0, 260)
        pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal")) 
        pen.goto(0, 240)
        pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Score 10 to pass level 1", align="center", font=("Courier", 10, "normal"))

        
        

    if level == 1:
        enemy.shape("enemy.gif")
        pen.goto(0, 260)
        pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal")) 
        pen.goto(0, 240)
        pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Score 10 to pass level 1", align="center", font=("Courier", 10, "normal"))

    if level == 2:
        enemy.shape("2nd_enemy.gif")
        pen.goto(0, 260)
        pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal")) 
        pen.goto(0, 240)
        pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Score 15 to pass level 2", align="center", font=("Courier", 10, "normal"))

    if level == 3:
        enemy.shape("3nd_enemy.gif")
        pen.goto(0, 260)
        pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal")) 
        pen.goto(0, 240)
        pen.write("Press Alt to pause", align="center", font=("Courier", 12, "normal"))
        pen.goto(0, 220)
        pen.write("Score 20 to Win", align="center", font=("Courier", 10, "normal"))

    wn.update() 

wn.mainloop()