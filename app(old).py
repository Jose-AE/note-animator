import turtle

NOTE_RANGE = 5
COLUMNS_RANGE = 10

BG_COLOR = (173,216,230)
NOTE_COLOR = (1, 87, 155)

WINDOW_WIDTH =1600
WINDOW_HEIGHT = 900
START_OFFSET = 200

#setup screen size 
turtle.Screen().setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, startx=None, starty=None)#setup(WINDOW_WIDTH, WINDOW_HEIGHT)

#bg color 
turtle.colormode(255)
turtle.Screen().bgcolor(BG_COLOR[0],BG_COLOR[1],BG_COLOR[2])

#turtle settings 
turtle.speed(0)
turtle.hideturtle()

def MoveTo(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def MoveToStart():
    MoveTo(-WINDOW_WIDTH/2 +START_OFFSET, -WINDOW_HEIGHT/2 +START_OFFSET)
   
    

def DrawCircle(radius, color):

    turtle.color(1, 87, 155)
    
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    


def DrawNote(note_pos, note_num):
    MoveToStart()
    
    #MOVE X POS 
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(50*note_pos)
    turtle.pendown()

    #MOVE Y POS 
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(75*note_num)
    turtle.pendown()
    
    DrawCircle(40,1)
    
for i in range(5):
    DrawNote(i,i)

def PlayNote(note_num):
    pass


turtle.done()