import os
import random
import turtle
turtle.fd(0)
turtle.speed(1)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
class Game():	
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

class Bullet(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.hideturtle()
		self.speed = 0
		self.shape("arrow")
		# self.speed(0)
		self.penup()
		self.color("white")
		self.fd(0)
		self.goto(0, 0)

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
	
	def move(self):
		self.fd(10)
	def turn_left(self):
		self.lt(30)
	def turn_right(self):
		self.rt(30)
	def accelerate(self):
		self.move()
		self.speed = self.speed + 1

class Enemy1(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(3)
		self.penup()
		self.color(color)
		self.fd(0)
		self.setposition(startx, starty)
		self.speed = 6
	
	shoot = 8 # shoots after 8 interval

	bullet1 = Bullet()

  	def move(self):
		self.lt(90)
		self.fd(100)
		self.shoot = self.shoot - 1
		if self.shoot==0:
			self.enemy1_fire() #shoot towards player
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

# enemy1 = Enemy1("circle", "red", 50, -50)

num_Enemy1 = 5
enemies1 = []
for i in range(num_Enemy1):
	b = Enemy1("circle", "red", random.randint(-180,180), random.randint(-180,180))
	enemies1.append(b)


player = Player("triangle", "white", 0, -290)

#key bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
#turtle.onkey(player.brake,"Down")

while True:
	for enemy1 in enemies1:
		enemy1.move()

		if (enemy1.bullet1.ycor()>275 or enemy1.bullet1.xcor()>275 or enemy1.bullet1.ycor()<-275 or enemy1.bullet1.xcor()<-275):
			enemy1.bullet1.hideturtle()
			enemy1.bullet1.clear()

	# enemy2.move()


	# if bulletstate1=="fire":
	# 	y = bullet1.ycor()
	# 	y = y - 900
	# 	bullet1.sety(y)

	# if bulletstate2=="fire":
	# 	y = bullet2.ycor()
	# 	y = y - 900
	# 	bullet2.sety(y)


	

	
	# if (bullet2.ycor()>275 or bullet2.xcor()>275 or bullet2.ycor()<-275 or bullet2.xcor()<-275):
	# 	bullet2.hideturtle()
	# 	bulletstate2="ready"

delay = raw_input("Press enter to finish. > ")