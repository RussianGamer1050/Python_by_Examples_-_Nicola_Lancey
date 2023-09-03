import turtle

turtle.color('black', 'black')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(25)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(50)

turtle.pendown()
turtle.color('black', 'white')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(25)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(50)

turtle.pendown()
turtle.color('black', 'gray')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(25)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.exitonclick()
