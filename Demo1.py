# python 2.7
import turtle
import os
import math

#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#set borders for the game 
border_pen = turtle.Turtle() # turtle for creating the boundary will now be called border_pen
border_pen.speed(0) # 0 is fastest speed and this sets the speed of the turtle
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300) #move the turtle towards the left edge
border_pen.pendown() # draw when the turtle moves
border_pen.pensize(3) # 3 pixel wide line

# create a square border for the game to appear by making the turtle draw 4 lines of same length
# at right angles
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#create player turtle
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup() # no drawing when the turtle moves
player.speed(0)
player.setposition(0,-250) # set players appearing position, will stay here for the rest of the game unless moved
player.setheading(90)
player.showturtle()

#player movement (L and R, associate them with keys), may not be required by us
playerspeed = 15
def move_left(): # set the updated x coordinates such that for every button press, it moves left by 15 pixels
    x = player.xcor()
    x = x - playerspeed
    if (x<-280): # boundary checking
        x = -280
    player.setx(x) # associate the new value of x to the player turtle

def move_right(): # set the updated x coordinates such that for every button press, it moves right by 15 pixels
    x = player.xcor()
    x = x + playerspeed
    if (x>280):  # boundary checking
        x = 280
    player.setx(x) # associate the new value of x to the player turtle

def fire_bullet():
    #the bullet will travel up from the player's position
    global bulletstate # enable modifying global var from inside of function
    if bulletstate == "ready":
        bulletstate = "fire"
        bullet.showturtle()
        x = player.xcor()
        y = player.ycor()
        bullet.speed(0) # fastest speed specified here separately than the bullet's actual speed
        bullet.setposition(x,y+10) # bullet will appear just above the player
        print(bulletspeed,bullet.xcor(),bullet.ycor(),bulletstate)
    # the movement of the bullet will be defined in the game loop

def isCollision(t1,t2): #calculate distance between bullet and enemy and if
    # less than a threshold, a collision happens
    x_dist = t1.xcor()-t2.xcor()
    y_dist = t1.ycor()-t2.ycor()
    distance = math.sqrt(x_dist**2 + y_dist**2)
    if distance<15:
        return True
    else:
        return False



#create key bindings
turtle.listen() # collect key events
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

# create 1 invader
enemy = turtle.Turtle()
enemy.color("red")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)
enemyspeed = 2

# create a bullet for the player
bullet  = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5) # length and breadth of bullet
bullet.hideturtle() 
# bullet starts out hidden, triggered by spacebar and once fired, it cannot change
# for the last point, maintain states. ready -> not fired, fire -> fired as global states

bulletspeed = 10

bulletstate = "ready"

# main game loop
while(True):
    x = enemy.xcor()
    x = x + enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280:
        enemyspeed  = enemyspeed * (-1) # change speed direction to left when at right boundary
        y = enemy.ycor() # drop down 40 pixels everytime it hits border
        y = y - 40
        enemy.sety(y)


    if enemy.xcor() < -280:
        enemyspeed  = enemyspeed * (-1) # change speed direction to right when at left boundary
        y = enemy.ycor() # drop down 40 pixels everytime it hits border
        y = y - 40
        enemy.sety(y)

    # move bullet
    if bulletstate=="fire":
        y = bullet.ycor()
        y = y + bulletspeed
        bullet.sety(y)

    #bullet border check
    if bullet.ycor()>275:
        bullet.hideturtle()
        bullet.sety(-240)
        bulletstate="ready"
    
    #check collision between bullet and enemy
    if (isCollision(bullet,enemy)):
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400) #avoid future collision with the same bullet
        enemy.setposition(-200,250) # enemy got hit so moved to initial place


delay = raw_input("Press enter to finish")
