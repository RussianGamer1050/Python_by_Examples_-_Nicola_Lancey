import turtle, random
turtle.begin_fill()
for i in range(0, 8):
    turtle.color(random.choice(['red', 'black', 'blue', 'gray', 'green', 'yellow']))
    turtle.forward(50)
    turtle.right(45)
turtle.exitonclick()
