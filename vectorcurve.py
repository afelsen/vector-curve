import turtle
import math

xangle = 30
scale = 10
xmin = -1*scale
ymin = -1*scale
xmax = scale
ymax = scale

def setUpWindow(screen_object):
    '''
        Sets up the window ranging from -360 to 360 in the x direction and -1 to 1 in the y direction
        args: screen_object(turtle.Screen) - The screen that is being set up
        returns: None
    '''
    screen_object.setworldcoordinates(xmin,ymin,xmax,ymax)

def setUpAxis(turtle_object):
    '''
        Draws a 3D axis
        args: turtle_object(turtle.Turtle) - The turtle that is drawing the axis
        returns: None
    '''

    turtle_object.pendown()
    turtle_object.goto(0,ymax)
    turtle_object.goto(0,ymin)
    turtle_object.goto(0,0)
    turtle_object.goto(xmax,0)
    turtle_object.goto(xmin,0)
    turtle_object.goto(0,0)
    turtle_object.left(90-xangle)
    turtle_object.forward(xmax)
    turtle_object.left(180)
    turtle_object.forward(xmax*2)
    turtle_object.left(90-xangle)


def isInScreen(turtle_object):
    '''
        Checks if the turtle is in the screen
        args: turtle_object(turtle.Turtle) - The turtle that is being checked
        returns: (bool)
    '''
    x = turtle_object.xcor()
    y = turtle_object.ycor()
    if (x > xmax or x < xmin or y > ymax or y < ymin):
        return False
    else:
        return True

def toroidalspiralx(t):
    return (scale*.75+math.sin(20*t))*math.cos(t)
def toroidalspiraly(t):
    return (scale*.75+math.sin(20*t))*math.sin(t)
def toroidalspiralz(t):
    return math.cos(20*t)

def helixx(t):
    return scale*.5*math.cos(t)
def helixy(t):
    return scale*.5*math.sin(t)
def helixz(t):
    return t/5

def parabaloidhelixx(t):
    return t*scale*.0015*math.cos(t)
def parabaloidhelixy(t):
    return t*scale*.0015*math.sin(t)
def parabaloidhelixz(t):
    return (t**2)/500

def xsqrdonfnx(t):
    return t*scale*.0015*math.cos(t)
def xsqrdonfny(t):
    return t*scale*.0015*math.sin(t)
def xsqrdonfnz(t):
    return (xsqrdonfnx(t)**2+xsqrdonfny(t)**2)**.5-3

def vector(turtle_object,function_dictionary):
    '''
        Graphs a vector valued function in 3D space
        args: turtle_object(turtle.Turtle) - the Turtle that draws the points
        returns: None
    '''

    t=function_dictionary["tlowerdomain"]
    turtle_object.penup()
    xarray = []
    yarray = []

    while isInScreen(turtle_object) and t<function_dictionary["tupperdomain"]:
        x = function_dictionary["xfunc"](t)
        y = function_dictionary["yfunc"](t)
        z = function_dictionary["zfunc"](t)

        xcor = y-x*(math.sin(math.radians(xangle)))
        ycor = z-x*(math.cos(math.radians(xangle)))
        turtle_object.goto(0,0)
        turtle_object.goto(xcor, ycor )
        turtle_object.dot()
        t += function_dictionary["tfrequency"]
        xarray.append(xcor)
        yarray.append(ycor)
    connectEvery5th(turtle_object,xarray,yarray)

def connectPoints(turtle_object,xarray,yarray):
    '''
        Connects the points drawn by vector()
        args: turtle_object(turtle.Turtle) - the Turtle that draws the curve
        returns: None
    '''
    turtle_object.penup()
    turtle_object.goto(xarray[1],yarray[1])
    turtle_object.pendown()
    turtle_object.color("red")

    for i in range(len(xarray)):
        turtle_object.goto(xarray[i],yarray[i])
def connectEvery5th(turtle_object,xarray,yarray):
    turtle_object.penup()
    turtle_object.goto(xarray[1],yarray[1])
    turtle_object.pendown()
    turtle_object.color("red")

    for i in range(6):
        for i in range(i,len(xarray),6):
            turtle_object.goto(xarray[i],yarray[i])
        turtle_object.penup()
        turtle_object.goto(xarray[1],yarray[1])
        turtle_object.pendown()

def main():

    torodialspiral = {"xfunc": toroidalspiralx, "yfunc": toroidalspiraly, "zfunc": toroidalspiralz, "tlowerdomain": 0, "tupperdomain": 2*math.pi, "tfrequency": math.pi/200}

    helix = {"xfunc": helixx, "yfunc": helixy, "zfunc": helixz, "tlowerdomain": 0, "tupperdomain": 6*math.pi, "tfrequency": math.pi/20}

    parabaloidhelix = {"xfunc": parabaloidhelixx, "yfunc": parabaloidhelixy, "zfunc": parabaloidhelixz, "tlowerdomain": 0, "tupperdomain": 100*math.pi, "tfrequency": math.pi/5}

    xsqrdonfn = {"xfunc": xsqrdonfnx, "yfunc": xsqrdonfny, "zfunc": xsqrdonfnz, "tlowerdomain": 0, "tupperdomain": 10000, "tfrequency":1}

    tur = turtle.Turtle()
    wn = turtle.Screen()
    tur.shape("turtle")
    tur.speed(0)
    tur.penup()
    setUpWindow(wn)
    setUpAxis(tur)

    vector(tur,xsqrdonfn)

    wn.exitonclick()
main()
