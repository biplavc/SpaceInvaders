# python 2.7 and turtle library

import os
import random

import sys
sys.stdout=open("test.txt","w")

#Import the Turtle module
import turtle
#Required by MacOSX to show the window
turtle.fd(0)
#Set the animations speed to the minimum
turtle.speed(6)
#Change the background color
turtle.bgcolor("black")
#Hide the default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

class Game():
	# def __init__(self):
	# 	self.level = 1
	# 	self.score = 0
	# 	self.state = "playing"
	# 	self.pen = turtle.Turtle()
	# 	self.lives = 3
		
	def draw_border(self):
		#Draw border
		self.pen = turtle.Turtle()
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()

game = Game()
game.draw_border()

bulletstate1 = "ready"
bulletstate2 = "ready"

def enemy1_fire():
	#the bullet will travel up from the player's position
	global bulletstate1 # enable modifying global var from inside of function
	if bulletstate1 == "ready":
		bulletstate1 = "fired"
		bullet1.showturtle()
		x = enemy1.xcor() # get the coordinates at the time of firing
		y = enemy1.ycor()
		bullet1.speed = 6 # slowest speed 
		bullet1.setposition(x,y) # bullet will appear just above the player
		# bullet1.goto(player.xcor,player.ycor) STATEMENT NOT WORKING
		#print(bulletspeed,bullet.xcor(),bullet.ycor(),bulletstate1)

def enemy2_fire():
	#the bullet will travel up from the player's position
	global bulletstate2 # enable modifying global var from inside of function
	if bulletstate2 == "ready":
		bulletstate2 = "fired"
		bullet2.showturtle()
		x = enemy2.xcor()
		y = enemy2.ycor()
		bullet2.speed = 6
		bullet2.setposition(x,y) # bullet will appear just above the player
		# bullet2.goto(player.xcor,player.ycor) STATEMENT NOT WORKING
		#print(bulletspeed,bullet.xcor(),bullet.ycor(),bulletstate2)
		

class Player(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 6
		self.left(90)
		#self.mode("logo")  
	
	def move(self):
		self.fd(self.speed)
	
	def turn_left(self):
		self.move()
		self.lt(30)
	def turn_right(self):
		self.move()
		self.rt(30)
	def accelerate(self):
		self.move()
		self.speed = self.speed + 1
	def brake(self):
		self.speed = self.speed - 1

class Enemy1(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(3) #animation speed
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1
		#self.mode("logo")
	
	shoot = 4 # shoots after 4 interval

  	def move(self):
		self.lt(90)
		self.fd(150)
		self.shoot = self.shoot - 1
		if self.shoot==0:
			enemy1_fire() #shoot below, better if can be directed at player
			self.shoot = 4

class Enemy2(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1
		#self.mode("logo")

	shoot = 2 # shoots after 2 interval

	def move(self):
		self.fd(100)
		self.rt(30)
		self.shoot= self.shoot-1
		if self.shoot==0:
			enemy2_fire() #shoot towards player
			self.shoot = 2

enemy1 = Enemy1("circle", "red", 50, -50)
enemy2 = Enemy2("square", "blue", -10, 200)
player = Player("triangle", "white", 0, 0)


#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.brake,"Down")

# create a bullet for the enemy1
bullet1  = turtle.Turtle()
bullet1.color("yellow")
bullet1.shape("triangle")
bullet1.penup()
bullet1.shapesize(0.3,0.3) # length and breadth of bullet
bullet1.hideturtle()
bullet1.speed(3)
bullet1.speed = 6

# create a bullet for the enemy2
bullet2  = turtle.Turtle()
bullet2.color("yellow")
bullet2.shape("square")
bullet2.penup()
bullet2.shapesize(0.4,0.4) # length and breadth of bullet
bullet2.hideturtle()
bullet2.speed(3)
bullet2.speed = 6



while True:
	print("bulletstate1 = " + str(bulletstate1) + ";" "bulletstate2 =" + str(bulletstate2))
	print ("bullet1's positions are (" + str(bullet1.xcor()) + ";" + str(bullet1.ycor())+ ")")
	print ("bullet2's positions are (" + str(bullet2.xcor()) + ";" + str(bullet2.ycor())+ ")"+ "\n")

	enemy1.move()
	enemy2.move()

	# if player.xcor>290:
	# 	player.setx(290)
	# if player.xcor<-290:
	# 	player.setx(-290)
	# if player.ycor>290:
	# 	player.sety(290)
	# if player.ycor<-290:
	# 	player.sety(-290)



	if bulletstate1=="fired":
		y = bullet1.ycor()
		y = y - bullet1.speed
		bullet1.sety(y)

	if bulletstate2=="fired":
		y = bullet2.ycor()
		y = y - bullet2.speed
		bullet2.sety(y)

	if (bullet1.ycor()>275 or bullet1.xcor()>275 or bullet1.ycor()<-275 or bullet1.xcor()<-275):
		bullet1.hideturtle()
		# bullet1.sety(enemy1.ycor)
		# bullet1.setx(enemy1.xcor)
		bulletstate1="ready"

	
	if (bullet2.ycor()>275 or bullet2.xcor()>275 or bullet2.ycor()<-275 or bullet2.xcor()<-275):
		bullet2.hideturtle()
		# bullet2.sety(enemy2.ycor)
		# bullet2.setx(enemy2.xcor)
		bulletstate2="ready"

sys.stdout.close()
delay = raw_input("Press enter to finish. > ")