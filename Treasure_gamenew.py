#But better

#!/bin/python3
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

R = [255, 0, 0]  # red
Y = [255, 255, 0] # yellow
G = [0, 255, 0] # green
W = [255, 255, 255] # white
Bl=[0,0,0]
score=0


for turns in range(5):
  
  
  coinx=randint(0,7)
  coiny=randint(0,7)
  print(coinx, coiny)
  
  sense.set_pixel(coinx, coiny, Y)
  sleep(2)
  sense.clear()
  
  x=randint(0,7)
  y=randint(0,7)
  sense.set_pixel(x, y, W)
  
  while True:
    e = wait_for_move()
    if e.direction == DIRECTION_MIDDLE:
      
      if x == coinx and y== coiny:
        sense.set_pixel(x,y,G)
        score+= 1
      else:
        sense.set_pixel(x,y,R)
        
      sleep(1)
      sense.clear()
      break;
    sense.clear()
    if e.direction== DIRECTION_UP and y>0:
      y= y-1
    elif e.direction == DIRECTION_DOWN and y<7:
      y=y+1
    elif e.direction == DIRECTION_LEFT and x>0:
      x= x - 1
    elif e.direction == DIRECTION_RIGHT and x<7:
      x=x+1
    sense.set_pixel(x,y,W)
        
for turns in range(3):
  coin1x=randint(0,7)
  coin1y=randint(0,7)
  hits=0
  
  coin2x=randint(0,7)
  coin2y=randint(0,7)
  print(coinx, coiny)
  
  sense.set_pixel(coin1x, coin1y, Y)
  sense.set_pixel(coin2x, coin2y, Y)
  
  sleep(2)
  sense.clear()
  
  x=randint(0,7)
  y=randint(0,7)
  sense.set_pixel(x, y, W)
  
  while True:
    e = wait_for_move()
    if e.direction == DIRECTION_MIDDLE:
      
      if x == coin1x and y== coin1y and hits !=1:
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sense.set_pixel(coin2x, coin2y, Y)
        sleep(1)
        sense.set_pixel(coin2x, coin2y, Bl)
        
        
        
      elif x == coin2x and y== coin2y and hits != 1:
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sense.set_pixel(coin1x, coin1y, Y)
        sleep(1)
        sense.set_pixel(coin1x, coin1y, Bl)
      elif hits ==1 and x == coin2x and y== coin2y :
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sleep(1)
    
      elif hits ==1 and x == coin1x and y== coin1y :
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sleep(1)
                
    
        
      else:
        sense.set_pixel(x,y,R)
        sleep(1)
        sense.clear()
        break;
      

      
      sense.clear()
      if hits == 2:
          
          break;
    
    sense.clear()
    if e.direction== DIRECTION_UP and y>0:
      y= y-1
    elif e.direction == DIRECTION_DOWN and y<7:
      y=y+1
    elif e.direction == DIRECTION_LEFT and x>0:
      x= x - 1
    elif e.direction == DIRECTION_RIGHT and x<7:
      x=x+1
    sense.set_pixel(x,y,W)
for turns in range(2):
  coin1x=randint(0,7)
  coin1y=randint(0,7)
  hits=0
  
  coin2x=randint(0,7)
  coin2y=randint(0,7)
  print(coinx, coiny)
  
  sense.set_pixel(coin1x, coin1y, Y)
  sense.set_pixel(coin2x, coin2y, Y)
  
  sleep(2)
  sense.clear()
  
  x=randint(0,7)
  y=randint(0,7)
  sense.set_pixel(x, y, W)
  
  while True:
    e = wait_for_move()
    if e.direction == DIRECTION_MIDDLE:
      
      if x == coin1x and y== coin1y and hits !=1:
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sleep(1)
        sense.set_pixel(coin2x, coin2y, Y)
        sleep(.05)
        sense.set_pixel(coin2x, coin2y, Bl)
        
        
        
      elif x == coin2x and y== coin2y and hits != 1:
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sleep(1)
        sense.set_pixel(coin1x, coin1y, Y)
        sleep(.05)
        sense.set_pixel(coin1x, coin1y, Bl)
      elif hits ==1 and x == coin2x and y== coin2y :
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sleep(1)
    
      elif hits ==1 and x == coin1x and y== coin1y :
        sense.set_pixel(x,y,G)
        score+= 1
        hits += 1
        sleep(1)
                
    
        
      else:
        sense.set_pixel(x,y,R)
        sleep(1)
        sense.clear()
        break;
      

      
      sense.clear()
      if hits == 2:
          
          break;
    
    sense.clear()
    if e.direction== DIRECTION_UP and y>0:
      y= y-1
    elif e.direction == DIRECTION_DOWN and y<7:
      y=y+1
    elif e.direction == DIRECTION_LEFT and x>0:
      x= x - 1
    elif e.direction == DIRECTION_RIGHT and x<7:
      x=x+1
    sense.set_pixel(x,y,W)
    
sense.show_message("Score: " + str(score))
print (score)



