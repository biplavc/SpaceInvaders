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
turtle.delay(0)
turtle.tracer(20,0)
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
	moving_speed = 1

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

	# Enemy1 class defined
	def mobility_pattern(self):
		x = enemy1.xcor()
		x += enemy1.moving_speed
		enemy1.setx(x)

		if x < -390:
			enemy1.moving_speed *= -1

		if x > 390:
			enemy1.moving_speed *= -1

		# self.lt(10)
		# self.fd(10)

num_Enemy1 = 1
enemies1 = []
for i in range(num_Enemy1):
	b = Enemy1("circle", "red", random.randint(-180,180), random.randint(-100,250))
	enemies1.append(b)

# Enemy1 class defined

# Define Enemy2 class

class Enemy2(turtle.Turtle):

	a=[]

	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank2.gif")
		self.hideturtle
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
	

	def enemy2_fire(self):
		x = self.xcor()
		y = self.ycor()
		bullet2 = Bullet()
		bullet2.setposition(x,y) # bullet will appear just above the player
		bullet2.setheading(270)
		bullet2.showturtle()
		self.a.append(bullet2)

	def mobility_pattern(self):
		self.lt(100)
		self.fd(90)


num_Enemy2 = 1
enemies2 = []
for i in range(num_Enemy2):
	b = Enemy2("circle", "red", random.randint(-180,180), random.randint(-100,250))
	enemies2.append(b)

# Enemy2 class defined

# Define Enemy3 class

class Enemy3(turtle.Turtle):

	a=[]

	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank3.gif")
		self.hideturtle
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
	

	def enemy3_fire(self):
		x = self.xcor()
		y = self.ycor()
		bullet3 = Bullet()
		bullet3.setposition(x,y) # bullet will appear just above the player
		bullet3.setheading(270)
		bullet3.showturtle()
		self.a.append(bullet3)

num_Enemy3 = 1
enemies3 = []
for i in range(num_Enemy3):
	b = Enemy3("circle", "red", random.randint(-180,180), random.randint(-100,250))
	enemies3.append(b)

player = Player("triangle", "white", 0, -390)

#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
#turtle.onkey(player.brake,"Down")

freq1 = 600
freq2 = 300
freq3 = 450

while True:

	# enemy 1 loop

	for enemy1 in enemies1:

		enemy1.mobility_pattern()
		freq1 = freq1 - 1

		if  freq1 == 0:
			enemy1.enemy1_fire()
			print("Freq", freq1)
			freq1 = 600

		for bullet in enemy1.a:
			print("Bullet list length", len(enemy1.a))
			y = bullet.ycor()
			y1 = y - 1
			bullet.sety(y1)

		for bullet in enemy1.a:
			#Goes out of screen - delete the bullet
			if (bullet.ycor()>390 or bullet.xcor()>390 or bullet.ycor()<-390 or bullet.xcor()<-390):
				bullet.hideturtle()
				bullet.clear()
				enemy1.a.remove(bullet)


	# enemy 2 loop

	for enemy2 in enemies2:
		enemy2.mobility_pattern()
		freq2 = freq2 - 1
		if (freq2==0):
			enemy2.enemy2_fire()
			freq2 = 300

		for bullet in enemy2.a:
			y = bullet.ycor()
			y1 = y - 10
			bullet.sety(y1)

		for bullet in enemy2.a:
			if (bullet.ycor()>390 or bullet.xcor()>390 or bullet.ycor()<-390 or bullet.xcor()<-390):
				bullet.hideturtle()
				bullet.clear()
				enemy2.a.remove(bullet)

	# # enemy 3 loop
    #
	for enemy3 in enemies3:
		enemy3.fd(50)
		enemy3.rt(30)

		freq3 = freq3 - 1
		if (freq3==0):
			enemy3.enemy3_fire()
			freq3 = 450


		for bullet in enemy3.a:
			y = bullet.ycor()
			y1 = y - 10
			bullet.sety(y1)

		for bullet in enemy3.a:
			if (bullet.ycor()>390 or bullet.xcor()>390 or bullet.ycor()<-390 or bullet.xcor()<-390):
				bullet.hideturtle()
				bullet.clear()
				enemy3.a.remove(bullet)


delay = raw_input("Press enter to finish. > ")