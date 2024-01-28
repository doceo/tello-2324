## Progetto Tello 2E
## Partecipanti: Francesco Corcione, Fabio Iannaccone, Luca Antonio Niceforo, Fabrizio Perretti, Matteo Pierri, Ciro Solito, Flavio Zubbo

from djitellopy import Tello
import keyboard
import sys

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

print("Inserire valore per distanza, cm")

distanza = int(input(""))

if distanza > 50:
    print("Hai inserito un valore non valido")              
    sys.exit()

## Il ciclo serve per verificare se i tasti siano premuti 
    
while True:                                              
    if keyboard.read_key() == "w":
        tello.move_forward(distanza)
 
    if keyboard.read_key() == "s":
        tello.move_forward(distanza)
    
    if keyboard.read_key() == "a":
        tello.move_left(distanza)

    if keyboard.read_key() == "d":
        tello.move_right(distanza)
    
    if keyboard.read_key() == "q":
        tello.flip("forward")

    if keyboard.read_key() == "l":
        tello.land()

    if keyboard.read_key() == "t":
        tello.takeoff()


     
     
     
     
     
    


     

