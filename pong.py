#ping pong game using python

#part 1:Geting started
import turtle

wn= turtle.Screen()                   #to import screen
wn.title("ping Pong by aksa")         #to give tittle to the window
wn.bgcolor("black")                   #to give backgroundcolor to the window
wn.setup(width=800,height=600)        #to size the window
wn.tracer(0)                          #to stop the automatic screen updates

#paddle 1
paddle_1 = turtle.Turtle()           #impoting object "turtle" from the turtle module
paddle_1.speed(0)                    #to set the paddle speed to max
paddle_1.shape("square")             #to set the shape the paddle
paddle_1.color("white")              #to set the color
paddle_1.shapesize(stretch_wid=5,stretch_len=1) #to stretch the paddle to a rectangle,by default a swaure is 20*20
paddle_1.penup()                     #no drawing while moving
paddle_1.goto(-350,0)                #to align paddle in th leftmost of X axis


#paddle 2
paddle_2 = turtle.Turtle()           #impoting object "turtle" from the turtle module
paddle_2.speed(0)                    #to set the paddle speed to max
paddle_2.shape("square")             #to set the shape the paddle
paddle_2.color("white")              #to set the color
paddle_2.shapesize(stretch_wid=5,stretch_len=1) #to stretch the paddle to a rectangle,by default a swaure is 20*20
paddle_2.penup()                     #no drawing while moving
paddle_2.goto(+350,0)                #to align paddle in th leftmost of X axis

#ball
ball= turtle.Turtle()           #impoting object "turtle" from the turtle module
ball.speed(0)                    #to set the paddle speed to max
ball.shape("square")             #to set the shape the paddle
ball.color("white")              #to set the color
ball.penup()                     #no drawing while moving
ball.goto(0,0)                #to align paddle in th leftmost of X axis
ball.dy=-0.4                      #change in the y coordinate
ball.dx=0.4                      #change in the x coordinate

#functions
def paddle_1_up():
    y=paddle_1.ycor()         #assignes the value of y cordinate of paddle_1 to y
    y += 20                   #calculates new y coordinates
    paddle_1.sety(y)          #sets the new y coordinates to the paddle_1 


def paddle_1_down():
    y=paddle_1.ycor()         #assignes the value of y cordinate of paddle_1 to y
    y -= 20                   #calculates new y coordinates
    paddle_1.sety(y)          #sets the new y coordinates to the paddle_1 


def paddle_2_up():
    y=paddle_2.ycor()         #assignes the value of y cordinate of paddle_1 to y
    y += 20                   #calculates new y coordinates
    paddle_2.sety(y)          #sets the new y coordinates to the paddle_1 


def paddle_2_down():
    y=paddle_2.ycor()         #assignes the value of y cordinate of paddle_1 to y
    y -= 20                   #calculates new y coordinates
    paddle_2.sety(y)          #sets the new y coordinates to the paddle_1 

#keyboard binding
wn.listen()                   #listen for the keyboard
wn.onkeypress(paddle_1_up,"w")#when the user press w,call the fuction paddle_1_up
wn.onkeypress(paddle_1_down,"s")#when the user press w,call the fuction paddle_1_up
wn.onkeypress(paddle_2_up,"Up")#when the user press w,call the fuction paddle_1_up
wn.onkeypress(paddle_2_down,"Down")#when the user press w,call the fuction paddle_1_up

# Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)   # combining the coordinate of the ball
    ball.sety(ball.ycor() + ball.dy)
 
    #border checking
    if ball.ycor() >290:       #the top most y coordinate is 300,the ball has 20 diameter.
        ball.sety(290)         #the ball sops there
        ball.dy *= -1          #the ball reverses back

    if ball.ycor() <-290:       #the bottom most y coordinate is 300,the ball has 20 diameter.
        ball.sety(-290)         #the ball sops there
        ball.dy *= -1          #the ball reverses back
    
    if ball.xcor() > 390:       #the right most x coordinate is 400.diameer of the ball is 20
        ball.goto(0,0)          #the ball hoes to (0,0)
        ball.dx *=-1

    if ball.xcor() < -390:       #the left most x coordinate is 400.diameter of the ball is 20
        ball.goto(0,0)          #the ball hoes to (0,0)
        ball.dx *=-1

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor()<350 ) and (ball.ycor() < paddle_2 +40 and ball.ycor() >paddle_2.ycor()-40 ):   
       ball.setx(340)
       ball.dx *= -1