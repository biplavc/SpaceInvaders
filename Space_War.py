import os
import random

#Import the Turtle module
import turtle
#Required by MacOSX to show the window
turtle.fd(0)
#Set the animations speed to the maximum
turtle.speed(0)
#Change the background color
turtle.bgcolor("black")
#Hide the default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

class Player(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1
		self.left(90)
	
	def move(self):
		self.fd(self.speed)
	
	def turn_left(self):
		self.lt(30)
	def turn_right(self):
		self.lt(30)
	def accelerate(self):
		self.speed = self.speed + 1
	def brake(self):
		self.speed = self.speed - 1

class Enemy1(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1 #speed supposed to be low but not happening
	
	shoot = 4 # shoots after 4 interval

  	def move(self):
		self.lt(90)
		self.fd(150)

class Enemy2(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1 #speed supposed to be low but not happening

	shoot = 2 # shoots after 2 interval

	def move(self):
		self.fd(100)
		self.rt(30)

enemy1 = Enemy1("circle", "red", 250, 250)
enemy2 = Enemy2("square", "blue", 200, 200)
player = Player("triangle", "white", 0, 0)


#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.brake,"Down")







while True:
	player.move()
	enemy1.move()
	enemy2.move()

	#Create my player
	



















delay = raw_input("Press enter to finish. > ")