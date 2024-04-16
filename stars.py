import turtle as t
import random
def main():
	win = t.Screen()
	star = t.Turtle()
	star.shape('turtle')
	win.bgcolor('black')
	star.color('white')
	x = 300
	y = 250
	for draw in range(9):
		add_x = random.randint(75, 100)
		add_y = random.randint(0, 100)
		star.penup()
		star.fillcolor('white')
		star.goto(x, y)
		star.pendown()
		star.speed(6)
		star.begin_fill()
		draw_star(star, 5)
		star.end_fill()
		x -= add_x
		y -= add_y
		star.hideturtle()
def draw_star(tur, angle):
	for i in range(angle):
		tur.forward(60)
		tur.right(144)
if __name__ == '__main__':
	main()
