
import os
import random
import turtle

wn = turtle.Screen()
wn.bgpic("space_invaders_background_new.gif")
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
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
		self.fd(10)
	def turn_left(self):
		self.lt(30)
	def turn_right(self):
		self.rt(30)
	def accelerate(self):
		self.move()

# Define Enemy1 class

class Enemy1(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank1.gif")
		self.hideturtle
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
	

	bullet1 = Bullet()

	def enemy1_fire(self):
		x = self.xcor()
		y = self.ycor()
		self.bullet1.speed(3)
		self.bullet1.setposition(x,y) # bullet will appear just above the player
		self.bullet1.setheading(270)
		self.bullet1.showturtle()
		y1 = y - 900
		self.bullet1.sety(y1)

num_Enemy1 = 1
enemies1 = []
for i in range(num_Enemy1):
	b = Enemy1("circle", "red", random.randint(-180,180), random.randint(-100,250))
	enemies1.append(b)

# Enemy1 class defined

# Define Enemy2 class

class Enemy2(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank2.gif")
		self.hideturtle
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)

	bullet2 = Bullet()

	def enemy2_fire(self):
		x = self.xcor()
		y = self.ycor()
		self.bullet2.setposition(x,y) # bullet will appear just above the player
		self.bullet2.setheading(270)
		self.bullet2.showturtle()
		self.bullet2.speed(3)
		y1 = y - 900
		self.bullet2.sety(y1)


num_Enemy2 = 1
enemies2 = []
for i in range(num_Enemy2):
	b = Enemy2("square", "blue", random.randint(-180,180), random.randint(-100,250))
	enemies2.append(b)

# Enemy2 class defined

# Define Enemy3 class

class Enemy3(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank3.gif")
		self.hideturtle
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
	

	bullet3 = Bullet()

	def enemy3_fire(self):
		x = self.xcor()
		y = self.ycor()
		self.bullet3.setposition(x,y) # bullet will appear just above the player
		self.bullet3.setheading(270)
		self.bullet3.showturtle()
		self.bullet3.speed(3)
		y1 = y - 900
		self.bullet3.sety(y1)


num_Enemy3 = 1
enemies3 = []
for i in range(num_Enemy3):
	b = Enemy3("circle", "red", random.randint(-180,180), random.randint(-100,250))
	enemies3.append(b)

# Enemy3 class defined

player = Player("triangle", "white", 0, -390)

#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
#turtle.onkey(player.brake,"Down")

freq1 = 8
freq2 = 4
freq3 = 12

while True:
	for enemy1 in enemies1:
		enemy1.rt(25)
		enemy1.fd(60)
		freq1 = freq1 - 1
		if (freq1==0):
			enemy1.enemy1_fire()
			freq1 = 8

		if (enemy1.bullet1.ycor()>390 or enemy1.bullet1.xcor()>390 or enemy1.bullet1.ycor()<-390 or enemy1.bullet1.xcor()<-390):
			enemy1.bullet1.hideturtle()
			enemy1.bullet1.clear()


	for enemy2 in enemies2:
		enemy2.lt(30)
		enemy2.fd(60)
		freq2 = freq2 - 1
		if (freq2==0):
			enemy2.enemy2_fire()
			freq2 = 4

		if (enemy2.bullet2.ycor()>390 or enemy2.bullet2.xcor()>390 or enemy2.bullet2.ycor()<-390 or enemy2.bullet2.xcor()<-390):
			enemy2.bullet2.hideturtle()
			enemy2.bullet2.clear()


	for enemy3 in enemies3:
		enemy3.rt(90)
		enemy3.fd(80)
		freq3 = freq3 - 1
		if (freq3==0):
			enemy3.enemy3_fire()
			freq3 = 12

		if (enemy3.bullet3.ycor()>390 or enemy3.bullet3.xcor()>390 or enemy3.bullet3.ycor()<-390 or enemy3.bullet3.xcor()<-390):
			enemy3.bullet3.hideturtle()
			enemy3.bullet3.clear()

	


delay = raw_input("Press enter to finish. > ")