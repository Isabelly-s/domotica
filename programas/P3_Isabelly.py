Programa 3
Autor:Maria Isabelly Da Silva Cavalcante
Data:30/04/2025

"""   Maria Isabelly Da Silva Cavalcante, 07 de abril de 2025 """

from microbit import *
import music

while True:
    if  button_a.is_pressed():
        pin14.write_digital(1)
        sleep(5000)
        pin14.write_digital(0)
        music.play(music.RINGTONE)
