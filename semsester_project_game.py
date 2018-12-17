from sense_hat import SenseHat
from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# Just return the actions we are interested in
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e
      


#Colors list
r = [255, 0, 0]  # red
y = [255, 255, 0] # yellow
g = [0, 255, 0] # green
w= [255, 255, 255] # white
b=[0,0,0] #black

#All the objects and "sprites" we need
blank= [b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        ] #An easy template to buid pictures off of

sword= [b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,w,b,
        b,b,b,b,w,w,w,w,
        b,b,b,b,b,b,w,b,
        b,b,b,b,b,b,b,b,
        ] #The player's "sprite"
def s_up():
  s_direction=1
  sx1=6
  sy1=3
  sx2=6
  sy2=4
  sx3=6
  sy3=5
  sx4=6
  sy4=6
  sx5=5
  sy5=5
  sx6=7
  sy6=5
  sense.set_pixel(sx1,sy1,w)
  sense.set_pixel(sx2,sy2,w)
  sense.set_pixel(sx3,sy3,w)
  sense.set_pixel(sx4,sy4,w)
  sense.set_pixel(sx5,sy5,w)
  sense.set_pixel(sx6,sy6,w)
  

arrowd= [(2,1,w),(2,2,w),(2,3,r)] 

arrow=       [b,w,b,b,b,b,b,b,
        b,w,b,b,b,b,b,b,
        b,r,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        ]#The UNFINISHED base attacking arrow. May make different versions to move down screen but unlikley

arrowu=  [b,r,b,b,b,b,b,b,
        b,w,b,b,b,b,b,b,
        b,w,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        ]  
        
x=1
y1=0
y2=1
y3=2
lives=3


  


"""My idea with this is to make a game that has different direction arrows that come at you, and you have to match the direction to "beat" the arrow, much like that tower game I used to play.
The whole game will be set 90 degrees counterclockwise because thatll make it easier to play with all the connections. An arrow with a random direction will come down the screen slowly, and the player has to match that dierction with the joystick when it reaches them, and if they miss, they get a strike.
The arrows will get continously more frequent and faster moving, adding to the difficulty of the game. More to add later"""
sense.set_rotation(90)
sense.set_pixels(sword)
sleep(1)
for turns in range(2):
  print "Hi"
  if y1==4:
    print "Hello"

for turns in range(3):
  a_direction= randint(1,4)
  def move_down(time):
    while True:
     pass

    
      
  if a_direction==1:
    y1=2
    x1=1
    x2=1
    y2=1
    x3=1
    y3=0
  if a_direction == 2:
    y1=0
    y2=0
    y3=0
    x1=1
    x2=2
    x3=3
  if a_direction== 3:
    x1=1
    y1=2
    x2=1
    y2=1
    x3=1
    y3=0
  if a_direction==4:
    x1=1
    y1=0
    x2=1
    y2=1
    x3=1
    y3=2
    
  print a_direction
  s_direction=0
  score=0
  
  

    
    
    
  



  sense.set_pixel(x1,y1,w)
  sense.set_pixel(x2,y2,w)
  sense.set_pixel(x3,y3,r)
  

  while True:
    sense.clear()
    s_up()
    print "hi"
    
    
    
    y1+=1
    y2+=1
    y3+=1
    sense.set_pixel(x1,y1,w)
    sense.set_pixel(x2,y2,w)
    sense.set_pixel(x3,y3,r)
    sleep(2)
    
    
    
    if x1==12:
      e = wait_for_move()
      if e.direction== DIRECTION_UP and y>0:
        s_up()
      elif e.direction == DIRECTION_DOWN and y<7:
        y=y+1
      elif e.direction == DIRECTION_LEFT and x>0:
        x= x - 1
      elif e.direction == DIRECTION_RIGHT and x<7:
        pass
      if e.direction == DIRECTION_MIDDLE and s_direction == a_direction and y2==6:
        score+=1
        sense.clear()
        break
      elif y2!=6 and e.direction == DIRECTION_MIDDLE:
        lives -= 1
        sense.show_message("Lives = " +str(lives), scroll_speed= .01, text_colour=r)
      
        sense.clear()
        
      else:
        sense.clear()
    if y2 ==6:
        lives -= 1
        sense.show_message("Lives = " +str(lives), scroll_speed= .01, text_colour=r)
        break;
        
      
    
      
