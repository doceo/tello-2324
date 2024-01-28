## Progetto Tello 2E
## Partecipanti: Francesco Corcione, Fabio Iannaccone, Luca Antonio Niceforo, Fabrizio Perretti, Matteo Pierri, Ciro Solito, Flavio Zubbo

from djitellopy import TelloSwarm
import sys

swarm = TelloSwarm.fromIps([
    "Inserire ip drone 1",
    "Inserire ip drone 2",
    "Inserire ip drone 3"
])


altezza = int(input(""))

print("Inserire valore altezza, cm")

if altezza > 100:
    print("Numero non valido")
    sys.exit()


swarm.connect()
swarm.takeoff()

swarm.move_up(altezza)

swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))
swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))
swarm.flip("forward")
swarm.move_up(altezza)
swarm.flip("forward")

swarm.land()
swarm.end()