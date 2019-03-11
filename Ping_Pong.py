#importing the libraries required for the game
import turtle
import os

#creating screen
win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#scoring
score_a = 0  
score_b = 0
