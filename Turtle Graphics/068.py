import turtle, random
lines = random.randint(1, 10)
length = random.randint(1, 100)
angle = random.randint(1, 180)
for i in range(0, lines):
    turtle.forward(length)
    turtle.right(angle)
turtle.exitonclick()
