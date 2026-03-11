import turtle 

turtle.Screen().bgcolor("light yellow")
board = turtle.Turtle()

#rectangle
board.pensize(5)
board.color("lime green")
board.begin_fill()
for i in range(2):
  board.forward(250)
  board.left(90)
  board.forward(150)
  board.left(90)
board.end_fill()

board.penup()
board.right(180)
board.forward(90)


#triangle
board.pendown()
board.pensize(5)
board.color("Gold")
board.begin_fill()
for i in range(3):
  board.forward(200)
  board.right(120)
board.end_fill()

board.penup()
board.left(90)
board.forward(90)

#hexagon
board.pendown()
board.pensize(5)
board.color("Orange")
board.begin_fill()
for i in range(6):
    board.forward(100)
    board.left(60)
board.end_fill()

