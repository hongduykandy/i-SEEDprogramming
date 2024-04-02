# QUESTION 03

def plus(v1 , v2, v3):
    results = 0
    results = v1+v2+v3
    return results
hap = plus ( 100, 200, 300 )
print(hap)

# QUESTION 04

def f1():
    print(var)     

def f2():
    var =10
    print(var)

var = 100
f1()    # ==> 100
f2()    # ==> 10

# QUESTION 05

ss = "Python"

for i in range ( 0, len(ss)):
    print( ss[i] + '$', end = "")

# QUESTION 08

def myFunc(p1=1 , p2=2, p3=3):
    ret = p1+p2+p3
    return ret

print(myFunc())
print(myFunc(1))
print(myFunc(1,2))
print(myFunc(1,2,3))

# QUESTION 09

inStr, ouStr = "Python", ""
strLen = len(inStr)
for i in range(0,strLen):
    ouStr += inStr[-(i+1)]

print("reverse string --> %s" % ouStr)

# QUESTION 11_01

import re

def remove_special_characters(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

input_string = "....###COOKBOOK  @#$%^&*()_+{}[];:'\",.<>?/~`...1234"
cleaned_string = remove_special_characters(input_string)

print("Original String: \n ", input_string)
print("Cleaned String: \n ", cleaned_string)

# QUESTION 11_02

#Q11
def addNumber(num):
    results=0
    if num==0:
        results=0
    elif num==1:
        results=1
    else:
        results += num + addNumber(num-1)
    return results

print(addNumber(100))

# QUESTION 13

# Define function
import random
from tkinter.simpledialog import *

def getString():
    retStr = ''
    retStr = askstring( "Input_String" , "Enter A String in the dialog box:")
    return retStr

def getRGB():
    r, g, b = 0, 0, 0
    r=random.random()
    g=random.random()
    b=random.random()
    return (r, g, b)

def getXYAS(sw, sh):
    x, y, angle, size = 0, 0, 0, 0
    x = random.randrange(-sw/2, sw/2)
    y = random.randrange(-sh/2, sh/2)
    angle = random.randrange(0,360)
    size = random.randrange(10,50)
    return [x,y,angle, size]

# SOLVE QUESTION 13
from myTurtle_As1_Q13 import *
import turtle

inStr = ""
swidth, sheight = 500, 500

turtle.title('turtle')
turtle.shape("turtle")
turtle.setup(width=swidth+50, height=sheight + 50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr = getString()

radius = 1
angle = 10
for ch in inStr:
    
    r, g, b = getRGB()
    
    turtle.circle(radius,angle)
    radius += 2
    turtle.left(1)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=("Arial", 8, "normal"))

tuple.done()

