import random
from graphics import *



#helper functions

def left_wrap(car_object, width):  
    car_object.move(width, 0)

def right_wrap(car_object, width):
    car_object.move(-width,0)



def road(win,width,height):
    point1 = Point(0, height/6)
    point2 = Point(width, height/6 + 40)
    point3 = Point(0, 500)
    point4 = Point(width, 550)
    rectangles = [Rectangle(point1, point2), Rectangle(point3, point4)]
    for rectangle in rectangles:
        rectangle.draw(win)
        rectangle.setFill("gray")
        
#car class

'''class creates car based on an x and y point'''
class Car:
    def __init__(self, x, y): 
        
        
        
        point1 = Point(x-80, y-40)
        point2 = Point(x+80, y+40)
        point3 = Point(x-60, y+40)
        point4 = Point(x+60, y+40)
        point5 = Point(x-60, y-80)
        point6 = Point(x+60, y-40)
        

        radius1 = 20

        body = Rectangle(point1, point2)
        left_wheel =  Circle(point3, radius1)
        right_wheel = Circle(point4, radius1)
        box = Rectangle(point5, point6)
        
#list of parts for left and right (so that correct wheel is drawn on top)
        self.left_car = [right_wheel, body, left_wheel, box]
        self.right_car = [left_wheel, body, right_wheel, box]
        

 #parellel list of colors for various parts          
        self.car_colors = ["black", "blue", "black", "blue"]

    

    
    ''' draw_left method draws left car'''
                             

    def draw_left(self, win): 

        for i in range (len(self.left_car)):
            self.left_car[i].draw(win)
            self.left_car[i].setFill(self.car_colors[i])
  
    
    def draw_right(self, win): 
        
        for i in range (len(self.right_car)):
            self.right_car[i].draw(win)
            self.right_car[i].setFill(self.car_colors[i])


    def move(self, dx, dy):   
        for part in self.right_car:  
            part.move(dx, dy)

            

        '''create banner to display score and how many lives are left '''
class Banner:
    def __init__(self, message, x, y):
        # Creates a message at the top of the graphics window
        self.text = Text( Point( x, y), message )
        self.text.setFill( "black" )
        self.text.setTextColor( "black" )
        self.text.setSize( 20 )
        
    def draw( self, win ):
        #draws the text of the banner on the graphics window
        self.text.draw( win )
        self.win = win
        
    def setText( self, message ):
        #changes the text of the banner
        self.text.setText( message )

   
        


def main():

    #win and road 
    width, height = 1000, 700
    win = GraphWin("froggy game", width, height)
    road(win, width, height)



    #frog image
    frog_file = "frog.gif"

    frog = Image(Point( width/2, height *5/6), frog_file)
    frog.draw(win)
    

    
    #initializes variables
    car_lst = []
    lives = 3
    wins = 0


    #create score-keeper banner
    banner1 = Banner(str(lives) + ' life points left. '+ str(wins) + ' crossings',400, 50)
    banner1.draw(win)

    #create instruction banners above and below road
    banner2 = Banner("Click above the road to hop forward!", 750, 100)
    banner2.draw(win)
    banner3 = Banner("Click below the road to hop backwards!",750, 575)
    banner3.draw(win)
    
    

    #cars
    xs= [250, 400, 800, 200, 350, 400]
    ys = [250, 250, 250, 400, 400, 400]
    for i in range(6):
       car = Car(xs[i], ys[i])
       car_lst.append(car)
                    
    left_cars = car_lst[0:3]
    right_cars = car_lst[3:6]
       
    for car_object in left_cars:
        car_object.draw_left(win)

    for car_object in right_cars:
        car_object.draw_right(win)


    while lives > 0:
       
        
        for i in range(len(left_cars)):
           left_marker = left_cars[i].left_car[2].getCenter().getX()
           right_marker = right_cars[i].right_car[2].getCenter().getX()
           if left_marker < -20:
                left_wrap(left_cars[i], width)
           else:
                left_cars[i].move(-10, 0)
           if right_marker > width:
                right_wrap(right_cars[i], width)
           else:
                right_cars[i].move(10, 0)

        click = win.checkMouse()
        if click != None:
            if click.getY() < height/6:
                frog.move(0, -20)

            elif click.getY() > 550:
                frog.move(0, 20)

            for i in range(len(car_lst)):
                x_anchor = frog.getAnchor().getX()
                y_anchor = frog.getAnchor().getY()
                left_wheel_x = car_lst[i].left_car[2].getCenter().getX()
                right_wheel_x = car_lst[i].right_car[2].getCenter().getX()
                left_wheel_y = car_lst[i].left_car[2].getCenter().getY()
                high_y = left_wheel_y + 80

                x_bool = left_wheel_x < x_anchor < right_wheel_x
                y_bool = left_wheel_y < y_anchor < high_y

                if x_bool == True and y_bool == True:
                    lives = lives - 1
                    frog.undraw()
                    frog = Image(Point( width/2, height *5/6), frog_file)
                    frog.draw(win)
                    #update banner
                    banner1.setText(str(lives)+ ' life point(s) left. '+ str(wins) + ' crossing(s).')               
                    

                if y_anchor < height/6 :
                    wins = wins + 1
                    frog.undraw()
                    frog = Image(Point( width/2, height *5/6), frog_file)
                    frog.draw(win)
                    banner1.setText(str(lives)+ ' life point(s) left. '+ str(wins) + ' crossing(s).') 


                if lives == 0:
                    frog.undraw()
                    frog = Image(Point( width/2, height *5/6), frog_file)
                    frog.draw(win)
                    banner1.setText('Game Over.  Froggy crossed '+ str(wins) + ' time(s).')
                    
                       

    

main()
    
    
    
