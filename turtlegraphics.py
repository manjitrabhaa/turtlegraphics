from turtle import *
import turtle
manjit = turtle.Screen()
turtle.speed(50)
turtle.bgcolor("#fba0e3")
for Zeet in range(25):
	turtle.circle(7*Zeet)
	turtle.circle(-7*Zeet)
	turtle.left(Zeet)
turtle.exitonclick()
