import turtle
import winsound
import random

#Screen Setup
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders by Gerd Harlander")
wn.setup(width=600, height=600)
wn.tracer(0)
wn.bgpic("space_invaders_background.gif")

#Register shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")


#Globals
#Define Bullet state
bulletstate="ready"
score=0

#Draw Border
boarder_pen=turtle.Turtle()
boarder_pen.speed(0)
boarder_pen.color("white")
boarder_pen.penup()
boarder_pen.setposition(-300,-300)
boarder_pen.pensize(3)
boarder_pen.pendown()
for side in range(4):
    boarder_pen.fd(600)
    boarder_pen.lt(90)
boarder_pen.hideturtle()

#Draw the Score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.hideturtle()
score_pen.color("white")
score_pen.goto(0,260)
score_pen.write("Score: {}".format(score), align="center", font=("Courier",24,"normal"))

#Player Turtle
player=turtle.Turtle()
player.color("blue")
player.speed(0)
player.shape("player.gif")
player.penup()
player.goto(0,-250)
player.setheading(90)
playerspeed=15

#Functions
def move_player_left():
    px=player.xcor()
    px-=playerspeed
    if px>-290:
        player.setx(px)

def move_player_right():
    px=player.xcor()
    px+=playerspeed
    if px<290:
        player.setx(px)

def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
        x=player.xcor()
        y=player.ycor()+10
        bullet.goto(x,y)
        bullet.showturtle()
   
def isCollision(t1,t2):
    if t1.distance(t2)<15:
        return True
    else:
        return False
#keyboard Binding
wn.listen()
wn.onkeypress(move_player_left,"a")
wn.onkeypress(move_player_right,"d")
wn.onkeypress(fire_bullet,"space")

#enemy

#Chose number of enemies
number_of_enemies=5
#empty list of enemies
enemies=[]
#add enemies to the list
for i in range(number_of_enemies):
    #Cre
    enemies.append(turtle.Turtle())
for enemy in enemies:    
    enemy.shape("invader.gif")
    enemy.color("red")
    enemy.speed(0)
    enemy.penup()
    x=random.randint(-200,200)
    y=random.randint(100,250)

    enemy.goto(x,y)
    enemyspeed=0.1

#bullet
bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed=4

#Main Game Loop
while True:
    wn.update()

    #move the enemy
    for enemy in enemies:
        ex=enemy.xcor()
        ex+=enemyspeed
        enemy.setx(ex)
   
        if ex>280 or ex<-280:
            #Move all enemies down
            for e in enemies:                
                ey=e.ycor()
                ey-=40
                e.sety(ey)
            #Change Direction
            enemyspeed*=-1
          #Check for bullet leaving the screen
        if bullet.ycor()>280:
            bullet.hideturtle()
            bulletstate="ready"

        #check for collision between enemey and bullet
        if isCollision(bullet,enemy):
            #score
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            score_pen.clear()
            score+=10
            score_pen.write("Score: {}".format(score), align="center", font=("Courier",24,"normal"))
            #Reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.goto(0,-400)
            #Reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.goto(x,y)

    #move the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

  

    #check for collision enemy with player
    for enemy in enemies:
        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Gameover")