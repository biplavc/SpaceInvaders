# cd /media/biplav/Biplav_2/CollegeStuff/Research/DrReed/AgeofInformation/demo/game/Space_Invaders/program/SpaceInvaders/State_Removed.py
import os
import random
import turtle

wn = turtle.Screen()
wn.bgpic("space_invaders_background_new.gif")
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(None)
turtle.tracer(5,0)
turtle.register_shape("tank1.gif")
turtle.register_shape("tank2.gif")
turtle.register_shape("tank3.gif")


class Game():	
	def draw_border(self):
		#Draw border
		self.pen = turtle.Turtle()
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(0)
		self.pen.penup()
		self.pen.goto(-400, 400)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(800)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()

game = Game()
game.draw_border()

class Bullet(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.hideturtle()
		self.shape("arrow")
		self.penup()
		self.speed(0)
		self.color("white")
		self.fd(0)
		self.goto(0, 0)

class Player(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.hideturtle()
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.left(90)
		self.showturtle()
	
	def move(self):
		self.fd(10)
	def turn_left(self):
		self.lt(20)
	def turn_right(self):
		self.rt(20)
	def accelerate(self):
		self.move()

	# Bullet a[]


# Define Enemy1 class

class Enemy1(turtle.Turtle):

	a=[]

	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank1.gif")
		self.hideturtle
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
	

	def enemy1_fire(self):
		x = self.xcor()
		y = self.ycor()
		bullet1 = Bullet()
		bullet1.setposition(x,y) # bullet will appear just above the player
		bullet1.setheading(270)
		bullet1.showturtle()
		self.a.append(bullet1)

num_Enemy1 = 1
enemies1 = []
for i in range(num_Enemy1):
	b = Enemy1("circle", "red", random.randint(-180,180), random.randint(-100,250))
	enemies1.append(b)

# Enemy1 class defined


player = Player("triangle", "white", 0, -390)

#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
#turtle.onkey(player.brake,"Down")

freq1 = 8

while True:
	for enemy1 in enemies1:
		enemy1.rt(10)
		enemy1.fd(10)
		freq1 = freq1 - 1
		if (freq1==0):
			enemy1.enemy1_fire()
			freq1 = 8


		for bullets in enemy1.a:
			y = bullets.ycor()
			y1 = y - 10
			bullets.sety(y1)

		for bullets in enemy1.a:
			if (bullets.ycor()>390 or bullets.xcor()>390 or bullets.ycor()<-390 or bullets.xcor()<-390):
				bullets.hideturtle()
				bullets.clear()
				del bullets


delay = raw_input("Press enter to finish. > ")