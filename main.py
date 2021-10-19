
"""
This set of code (until the next multi-line comment) defines functions for drawing shapes.
"""

x= 200
#This variable controls the x-coordinate of the colored shapes.
y= 200
#This variable controls the y-coordinate of the colored shapes.

def outline():
#This function makes an black outline.  This outline is the black parts of the art. (Otherise the "frame")
    color("black")
    #The color is changed to black so it matches with the art. 
    pensize(7)
    #Tracy's path width is changed to an "7" to create the bold visual effect as seen in the art.
    for i in range(2):
    #This loop creates part of the outline
        forward(220)
        left(90)
        forward(20)
        left(90)
    left(90)
    forward(180)
    right(90)
    forward(220)
    right(90)
    forward(180)
    
    backward(180)
    right(90)
    
    forward(60)
    left(110)
    forward(165)
    right(180)
    
    forward(165)
    left(70)
    forward(60)
    left(126.5)
    forward(200)
    right(127.5)
    
    forward(160)
    right(64)
    forward(72)
    right(107.5)
    forward(127.4)
    left(120.5)
    
    forward(105)
    left(100)
    forward(136)
    left(139)
    forward(150)
    left(115.5)
    forward(105)
    
    right(213)
    
def positioning(x_coordinate, y_coordinate):
#This funtion with certain parameters controls the starting position of one set of colored shapes. 
    setposition(x_coordinate, y_coordinate)

def colored_shapes():
#This function creates one set of colored shapes (red, purple, blue, yellow, green, and orange shapes. 
    pensize(1)
    #The pensize is changed to one for more accuracy
    red_shape()
    #Calls out the function "red_shape" and draws the red shape
    purple_shape()
    #Calls out the function "purple_shape" and draws the purple shape
    blue_shape()
    #Calls out the function "blue_shape" and draws the blue shape
    yellow_shape()
    #Calls out the function "yellow_shape" and draws the yellow shape
    green_shape()
    #Calls out the function "green_shape" and draws the green shape
    orange_shape()
    #Calls out the function "orange_shape" and draws the orange shape

def red_shape():
#This function creates one of the four red shapes.
    color("red")
    #The color is changed to red for the red shape.
    begin_fill()
    #Tracy can now fill in shapes with color.
    forward(60)
    left(110)
    forward(165)
    right(180)
    end_fill()
    #Tracy stops the fill and fills in shapes with color. 
    
def purple_shape():
#This function creates one of the four purple shapes.
    color("purple")
    #The color is changed to purple for the purple shape.
    begin_fill()
    #Tracy can now fill in shapes with color.
    forward(165)
    left(70)
    forward(60)
    left(126.5)
    forward(200)
    right(127.5)
    end_fill()
    #Tracy stops the fill and fills in shapes with color. 

def blue_shape():
#This function creates one of the four blue shapes.
    color("blue")
    #The color is changed to blue for the blue shape.
    begin_fill()
    #Tracy can now fill in shapes with color.
    forward(160)
    right(64)
    forward(72)
    right(107.5)
    forward(127.4)
    left(120.5)
    end_fill()
    #Tracy stops the fill and fills in shapes with color. 

def yellow_shape():
#This function creates one of the four yellow shapes.
    color("yellow")
    #The color is changed to yellow for the yellow shape.
    begin_fill()
    #Tracy can now fill in shapes with color.
    forward(105)
    left(100)
    forward(136)
    left(139)
    forward(150)
    end_fill()
    #Tracy stops the fill and fills in shapes with color. 
    left(115.5)
    forward(105)
    left(106)
    
def green_shape():
#This function creates one of the four green shapes.
    color("green")
    #The color is changed to green for the green shape.
    begin_fill()
    #Tracy can now fill in shapes with color.
    forward(140)
    right(139)
    forward(95)
    right(90)
    forward(85)
    end_fill()
    #Tracy stops the fill and fills in shapes with color. 
    backward(85)
    right(90)
    forward(100)
    
def orange_shape():
#This function creates one of the four orange shapes.
    color("orange")
    #The color is changed to orange for the green shape.
    begin_fill()
    #Tracy can now fill in shapes with color.
    left(100)
    forward(28)
    right(75)
    forward(70)
    right(114)
    forward(56)
    right(90)
    forward(60)
    end_fill()
    #Tracy stops the fill and fills in shapes with color. 
    penup()
    #For positioning purposes, Tracy now cannot create an visible path
    backward(80)
    right(90)
    pendown()
    #Now that Tracy is properly positioned, Tracy can now create an visible path


"""
This set of code (until the next multi-line comment) asks the user for the program speed and controls the program speed.
"""

program_speed=input("How fast do you want the art to be drawn? (slow, medium, or fast): ") 
#sets the variable, "program_speed", to an input value. This value controls the speed of the art drawn.  Also prompts the user with the messsage "How fast do you want the art to be drawn? (slow, medium, or fast): " 
if program_speed=="slow":
#If the user types "slow" then the program speed is 3/11 of it's maximum potential.
    speed(3)
elif program_speed=="medium":
#If the user types "medium" then the program speed is 6/11 of it's maximum potential.
    speed(6)
else:
#If the user types anything else then the program speed is 11/11 of it's maximum potential.
    speed(0)



"""
This set of code (until the next multi-line comment) creates an 20x20 pixel filled-in black square in the center.
"""
penup()
#For positioning purposes, Tracy cannot draw an visible path
forward(20)
left(90)
pendown()
#Tracy now can draw because she is in an correct position
begin_fill()
#Tracy now has the ability to fill in shapes with color.
forward(20)
left(90)
for i in range(4):
#This loop repeats four times for the four sides.
    forward(40)
    left(90)
forward(40)
left(180)
end_fill()
#Tracy fills in shapes with color then loses her ability to do so.




"""
This set of code (until the next multi-line comment) draws everything except of the starting center square.  It calls out numerous functions for positioning and drawing.
"""
for i in range(4):
#This loop repeats 4 times for the 4 panels in the art. It draws the colored shapes and outlines while positioning for the next plane.
    penup()
    positioning(x, y)
    #Calls out the parameter function "positioning(x, y)" to position into drawing the colored shapes.
    
    if x==200:
    #This if-else statement changes the x values to approximetly the exact values needed in each iteration of the loop.
        x=200.001
    else:
        x=-200

    if y==200:
     #This if-else statement changes the x values to approximetly the exact values needed in each iteration of the loop.
        y=-200
    elif y==-200:
        y=-200.001
    else:
        y=200.001
        
    left(180)
    pendown()
    #Tracy can now draw
    colored_shapes()
    #Calls out the function "colored_shapes" to make the colored shapes
    outline()
    #Calls out the function "outline" to draw an outline
    penup()
    #Tracy now cannot draw for positioning purposes.
    forward(193)
    right(90)
    forward(55)
    left(90)

setposition(0,0)
#Tracy goes to the pitch-black center (0,0) so that she does not "show up" visually on the final product.