import random
score = 0
name = input("Enter your name: ")

r1 = random.randint(1, 50)
r2 = random.randint(1, 50)
q1 = str(r1) + ' - ' + str(r2) + ' = '
a = str(r1 - r2)
u1 = str(input(q1))
if u1 == a:
    score += 1
r1 = random.randint(1, 50)
r2 = random.randint(1, 50)
q2 = str(r1) + ' - ' + str(r2) + ' = '
a = str(r1 - r2)
u2 = str(input(q2))
if u2 == a:
    score += 1

s_file = open('Quiz.csv', 'a')
s_file.write(name + ', ' + q1 + u1 + ', ' + q2 + u2 + ', ' + str(score) + '\n')
s_file.close()
