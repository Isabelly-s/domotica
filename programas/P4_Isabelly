Autor: Maria Isabelly Da Silva Cavalcante
Data: 05/05/2025

 from microbit import *

p=pin2
angulo=0


while True:
  if button_b.is_pressed():
      angulo+=10
      p.write_analog(angulo)
      if angulo>=90:
          angulo=0
          p.write_analog(angulo)
