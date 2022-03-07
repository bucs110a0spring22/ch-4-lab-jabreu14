import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help


def drawSineCurve(myturtle=None):
  for i in range (-360, 360):
    num = math.sin(math.radians(i))
    print(num)
    myturtle.goto(i,num)

def drawTangentCurve(myturtle=None):
  myturtle.up()
  myturtle.goto(-360,0)
  myturtle.down()
  for i in range (-360, 360,):
    num = math.tan(math.radians(i))
    myturtle.goto(i,num)

def drawCosineCurve(myturtle=None):
  myturtle.up()
  myturtle.goto(-360,1)
  myturtle.down()
  for i in range (-360, 360):
    num = math.cos(math.radians(i))
    myturtle.goto(i,num)

def setupWindow(mywindow=None):
  mywindow.setworldcoordinates(-360,-1,360,1)
  mywindow.bgcolor("light blue")



def setupAxis(myturtle=None):
  myturtle.goto(0,1)
  myturtle.goto(0,-1)
  myturtle.goto(0,0)
  myturtle.goto(360,0)
  myturtle.goto(-360,0)
  
  
  


 
     






#########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(1)
    # drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
