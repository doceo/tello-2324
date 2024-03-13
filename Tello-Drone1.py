import time, cv2
from threading import Thread
from djitellopy import Tello
import sys 

print("Drone 1")

tello = Tello()

tello.connect()

## registrazione video 
keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
  
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()


recorder = Thread(target=videoRecorder)
recorder.start()



tello.takeoff()


print("Inserisce valore")

avanti = int("Input")

if avanti > 100:         
    sys.exit

tello.move_forward(avanti)

tello.move_left(90)
tello.move_forward(avanti)
tello.move_up(50)
tello.rotate_counter_clockwise(360)

tello.land()

keepRecording = False
recorder.join()