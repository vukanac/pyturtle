import turtle

turtle.shape("turtle")

turtle.speed(1) # 9999999
turtle.penup()
for i in range(16):
  turtle.write(i,align='center')
  turtle.forward(25)
turtle.goto(0,-5)
x=0
turtle.right(90)
for i in range(16):
  turtle.pendown()
  turtle.forward(400)
  turtle.penup()
  x+=25
  turtle.goto(x,-5)

turtle.exitonclick()
