
from turtle import *

def a():
    print("key is pressed!")
    forward(5)

def b():
    print("key is not pressed!")
    backward(30)

listen()
onkeypress(a," ")
onkeyrelease(b," ")
