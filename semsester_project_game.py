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
R = [255, 0, 0]  # red
Y = [255, 255, 0] # yellow
G = [0, 255, 0] # green
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

arrow=  [b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        ]#The UNFINISHED base attacking arrow. May make different versions to move down screen but unlikley
    

"""My idea with this is to make a game that has different direction arrows that come at you, and you have to match the direction to "beat" the arrow, much like that tower game I used to play.
The whole game will be set 90 degrees counterclockwise because thatll make it easier to play with all the connections. An arrow with a random direction will come down the screen slowly, and the player has to match that dierction with the joystick when it reaches them, and if they miss, they get a strike.
The arrows will get continously more frequent and faster moving, adding to the difficulty of the game. More to add later"""
sense.set_rotation(90)
sense.set_pixels(sword)
sleep(1)

for turns in range(5):



    if e.direction== DIRECTION_UP and y>0:
          y= y-1
    elif e.direction == DIRECTION_DOWN and y<7:
          y=y+1
    elif e.direction == DIRECTION_LEFT and x>0:
          x= x - 1
    elif e.direction == DIRECTION_RIGHT and x<7:
          x=x+1
