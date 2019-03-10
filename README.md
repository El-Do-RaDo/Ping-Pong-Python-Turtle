# Ping-Pong-Python-Turtle

Turtle: Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.

Imagine a robotic turtle starting at (0, 0) in the x-y plane. Give it the command turtle.forward(15), and it moves (on-screen!) 15 pixels in the direction it is facing, drawing a line as it moves. Give it the command turtle.left(25), and it rotates in-place 25 degrees clockwise.

By combining together these and similar commands, intricate shapes and pictures can easily be drawn.

The turtle module is an extended reimplementation of the same-named module from the Python standard distribution up to version Python 2.5.

It tries to keep the merits of the old turtle module and to be (nearly) 100% compatible with it. This means in the first place to enable the learning programmer to use all the commands, classes and methods interactively when using the module from within IDLE run with the -n switch.

The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways. Because it uses Tkinter for the underlying graphics, it needs a version of python installed with Tk support.


Turtle methods

Turtle motion

    Move and draw
        forward() | fd()
        backward() | bk() | back()
        right() | rt()
        left() | lt()
        goto() | setpos() | setposition()
        setx()
        sety()
        setheading() | seth()
        home()
        circle()
        dot()
        stamp()
        clearstamp()
        clearstamps()
        undo()
        speed()
    Tell Turtle’s state
        position() | pos()
        towards()
        xcor()
        ycor()
        heading()
        distance()
    Setting and measurement
        degrees()
        radians()

Pen control

    Drawing state
        pendown() | pd() | down()
        penup() | pu() | up()
        pensize() | width()
        pen()
        isdown()
    Color control
        color()
        pencolor()
        fillcolor()
    Filling
        filling()
        begin_fill()
        end_fill()
    More drawing control
        reset()
        clear()
        write()

Turtle state

    Visibility
        showturtle() | st()
        hideturtle() | ht()
        isvisible()
    Appearance
        shape()
        resizemode()
        shapesize() | turtlesize()
        settiltangle()
        tiltangle()
        tilt()

Using events
    onclick()
    onrelease()
    ondrag()
Special Turtle methods
    begin_poly()
    end_poly()
    get_poly()
    clone()
    getturtle() | getpen()
    getscreen()
    setundobuffer()
    undobufferentries()

