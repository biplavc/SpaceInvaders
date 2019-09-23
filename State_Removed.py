import os
import random
import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
turtle.register_shape("tank1.gif")
turtle.register_shape("tank2.gif")

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
		self.speed = 0
		self.shape("arrow")
		#self.speed(0)
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
		self.speed = 6
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
		self.speed = self.speed + 1

# Define Enemy1 class

class Enemy1(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = "tank1.gif")
		self.hideturtle()
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
		self.speed = 6
	
	shoot = 8 # shoots after 8 interval

	bullet1 = Bullet()

  	def move(self):
		self.showturtle()
		self.lt(90)
		self.fd(50)
		self.shoot = self.shoot - 1
		if self.shoot==0:
			self.enemy1_fire()
			self.shoot = 8

	def enemy1_fire(self):
		x = self.xcor()
		y = self.ycor()
		self.bullet1.speed = 0
		self.bullet1.setposition(x,y) # bullet will appear just above the player
		self.bullet1.setheading(270)
		self.bullet1.showturtle()
		self.bullet1.speed = 6
		y1 = y - 900
		self.bullet1.sety(y1)

# Enemy1 class defined

num_Enemy1 = 5
enemies1 = []
for i in range(num_Enemy1):
	b = Enemy1("circle", "red", random.randint(-180,180), random.randint(0,200))
	enemies1.append(b)

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
		self.speed = 3
	
	shoot = 4 # shoots after 8 interval

	bullet2 = Bullet()

  	def move(self):
		self.showturtle()
		self.fd(50)
		self.rt(30)
		self.shoot = self.shoot - 1
		if self.shoot==0:
			self.enemy2_fire()
			self.shoot = 4

	def enemy2_fire(self):
		x = self.xcor()
		y = self.ycor()
		self.bullet2.speed = 0
		self.bullet2.setposition(x,y) # bullet will appear just above the player
		self.bullet2.setheading(270)
		self.bullet2.showturtle()
		self.bullet2.speed = 6
		y1 = y - 900
		self.bullet2.sety(y1)

# Enemy2 class defined

num_Enemy2 = 5
enemies2 = []
for i in range(num_Enemy2):
	b = Enemy2("square", "blue", random.randint(-180,180), random.randint(0,200))
	enemies2.append(b)


# Define Enemy3 class

# class Enemy3(turtle.Turtle):
# 	def __init__(self, spriteshape, color, startx, starty):
# 		turtle.Turtle.__init__(self, shape = spriteshape)
# 		self.hideturtle
# 		self.speed(0)
# 		self.penup()
# 		self.color(color)
# 		self.fd(0)
# 		self.setposition(startx, starty)
# 		self.speed = 5
	
# 	shoot = 10 # shoots after 10 interval

# 	bullet3 = Bullet()

#   	def move(self): # zig zag with period 3
# 		#for i in range(3):
# 		self.setheading(225)
# 		self.fd(100)
# 		self.setheading(135)
# 		self.fd(100)
# 		# for j in range(3):
# 		# 	self.setheading(315)
# 		# 	self.fd(100)
# 		# 	self.setheading(45)
# 		# 	self.fd(100)	
# 		self.shoot = self.shoot - 1
# 		if self.shoot==0:
# 			self.enemy3_fire() #shoot towards player
# 			self.shoot = 10

# 	def enemy3_fire(self):
# 		x = self.xcor()
# 		y = self.ycor()
# 		self.bullet3.speed = 0
# 		self.bullet3.setposition(x,y) # bullet will appear just above the player
# 		self.bullet3.setheading(270)
# 		self.bullet3.showturtle()
# 		self.bullet3.speed = 6
# 		y1 = y - 900
# 		self.bullet3.sety(y1)

# # Enemy3 class defined

# num_Enemy3 = 5
# enemies3 = []
# for i in range(num_Enemy3):
# 	b = Enemy3("square", "yellow", random.randint(-180,180), random.randint(0,200))
# 	enemies3.append(b)

player = Player("triangle", "white", 0, -390)

#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
#turtle.onkey(player.brake,"Down")

while True:
	for enemy1 in enemies1:
		enemy1.move()

		if (enemy1.bullet1.ycor()>390 or enemy1.bullet1.xcor()>390 or enemy1.bullet1.ycor()<-390 or enemy1.bullet1.xcor()<-390):
			enemy1.bullet1.hideturtle()
			enemy1.bullet1.clear()


	for enemy2 in enemies2:
		enemy2.move()

		if (enemy2.bullet2.ycor()>390 or enemy2.bullet2.xcor()>390 or enemy2.bullet2.ycor()<-390 or enemy2.bullet2.xcor()<-390):
			enemy2.bullet2.hideturtle()
			enemy2.bullet2.clear()

	# for enemy3 in enemies3:
	# 	enemy3.move()

	# 	if (enemy3.bullet3.ycor()>390 or enemy3.bullet3.xcor()>390 or enemy3.bullet3.ycor()<-390 or enemy3.bullet3.xcor()<-390):
	# 		enemy3.bullet3.hideturtle()
	# 		enemy3.bullet3.clear()

delay = raw_input("Press enter to finish. > ")