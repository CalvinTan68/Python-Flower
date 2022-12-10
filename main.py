import turtle

turtle.Screen().bgcolor('black')
turtle.pencolor("red")
turtle.speed(1000)

for i in range(100):
  turtle.circle(180-i, 90)
  turtle.left(90)
  turtle.circle(180-i, 90)
  turtle.left(10)
  turtle.end_fill()
  
turtle.hideturtle()
