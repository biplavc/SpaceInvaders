# cd /media/biplav/Biplav_2/CollegeStuff/Research/DrReed/AgeofInformation/demo/game/Space_Invaders/program/SpaceInvaders/State_Removed.py
import os
import random
import turtle

#latest
wn = turtle.Screen()
wn.bgpic("space_invaders_background_new.gif")
turtle.fd(0)
turtle.speed(10)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(None)
turtle.delay(1)
# turtle.tracer(20,0)
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
		self.speed(8)
		self.color("white")
		self.fd(0)
		self.goto(0, 0)

class Player(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.hideturtle()
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.left(90)
		self.showturtle()
	
	def move(self):
		self.fd(5)
	def turn_left(self):
		self.lt(5)
	def turn_right(self):
		self.rt(5)
	def accelerate(self):
		self.move()

# Define Enemy1 class

class Enemy1(turtle.Turtle):

	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank1.gif")
		self.hideturtle
		self.speed(1)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
		self.bullet_list = []
	

	def enemy1_fire(self):
		x = self.xcor()
		y = self.ycor()
		bullet1 = Bullet()
		bullet1.setposition(x,y) # bullet will appear just above the player
		bullet1.setheading(270)
		bullet1.showturtle()
		self.bullet_list.append(bullet1)

num_Enemy1 = 1
enemies1 = []
for i in range(num_Enemy1):
	b = Enemy1("circle", "red", random.randint(-180,180), random.randint(-100,200))
	enemies1.append(b)

# Enemy1 class defined



class Enemy2(turtle.Turtle):

	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank2.gif")
		self.hideturtle
		self.speed(1)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
		self.bullet_list = []

	def enemy2_fire(self):
		x = self.xcor()
		y = self.ycor()
		bullet2 = Bullet()
		bullet2.setposition(x,y) # bullet will appear just above the player
		bullet2.setheading(270)
		bullet2.showturtle()
		self.bullet_list.append(bullet2)

num_Enemy2 = 1
enemies2 = []
for i in range(num_Enemy2):
	b = Enemy2("circle", "red", random.randint(-180,180), random.randint(-100,200))
	enemies2.append(b)

# Enemy3 class defined

class Enemy3(turtle.Turtle):

	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank3.gif")
		self.hideturtle
		self.speed(1)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
		self.bullet_list = []
	

	def enemy3_fire(self):
		x = self.xcor()
		y = self.ycor()
		bullet3 = Bullet()
		bullet3.setposition(x,y) # bullet will appear just above the player
		bullet3.setheading(270)
		bullet3.showturtle()
		self.bullet_list.append(bullet3)

num_Enemy3 = 1
enemies3 = []
for i in range(num_Enemy3):
	b = Enemy3("circle", "red", random.randint(-180,180), random.randint(-100,200))
	enemies3.append(b)

# Enemy3 class defined

player = Player("triangle", "white", 0, -390)

#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
#turtle.onkey(player.brake,"Down")

freq1 = 100
freq2 = 120
freq3 = 160

while True:

	# enemy 1 loop

	for enemy1 in enemies1:
		enemy1.rt(5)
		enemy1.fd(10)
		freq1 = freq1 - 1
		if (freq1==0):
			enemy1.enemy1_fire()
			freq1 = 100


		for bullet in enemy1.bullet_list:
			y = bullet.ycor()
			y1 = y - 5
			bullet.sety(y1)

		for bullet in enemy1.bullet_list:
			if (bullet.ycor()>390 or bullet.xcor()>390 or bullet.ycor()<-390 or bullet.xcor()<-390):
				bullet.hideturtle()
				bullet.clear()
				enemy1.bullet_list.remove(bullet)
				# print(len(enemy1.bullet_list))

	# enemy 2 loop

	for enemy2 in enemies2:
		enemy2.lt(5)
		enemy2.fd(10)
		freq2 = freq2 - 1
		if (freq2==0):
			enemy2.enemy2_fire()
			freq1 = 100


		for bullet in enemy2.bullet_list:
			y = bullet.ycor()
			y1 = y - 5
			bullet.sety(y1)

		for bullet in enemy2.bullet_list:
			if (bullet.ycor()>390 or bullet.xcor()>390 or bullet.ycor()<-390 or bullet.xcor()<-390):
				bullet.hideturtle()
				bullet.clear()
				enemy2.bullet_list.remove(bullet)
				# print(len(enemy2.bullet_list))



	# enemy 3 loop

	for enemy3 in enemies3:
		enemy3.rt(50)
		enemy3.fd(10)
		freq3 = freq3 - 1
		if (freq3==0):
			enemy3.enemy3_fire()
			freq1 = 100


		for bullet in enemy3.bullet_list:
			y = bullet.ycor()
			y1 = y - 10
			bullet.sety(y1)

		for bullet in enemy3.bullet_list:
			if (bullet.ycor()>390 or bullet.xcor()>390 or bullet.ycor()<-390 or bullet.xcor()<-390):
				bullet.hideturtle()
				bullet.clear()
				enemy3.bullet_list.remove(bullet)
				# print(len(enemy3.bullet_list))

delay = raw_input("Press enter to finish. > ")
