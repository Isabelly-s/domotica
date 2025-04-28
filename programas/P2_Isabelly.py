Programa 2
Autor: Maria Isabelly da Silva Cavalcante
Data:28/04/2025

from microbit import *

while True:
    luz = pin1.read_analog()
    if luz < 700:
        pin14.write_digital(1)

    else:
        pin14.write_digital(0)

sleep(1000)
