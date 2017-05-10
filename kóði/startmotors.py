import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

Motor1A = 16 #forward
Motor1B = 18 #backward
Motor1E = 22 #enabled

Motor2A = 11 #forward 23
Motor2B = 13 #backward 21
Motor2E = 15 #enabled 19

print("Creating first motor..")
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
print("Creating second motor..")
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

moving = "nothing"

print("Initializing pygame loop..")
pygame.init()
size = [100, 100]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving = "left"
                GPIO.output(Motor1A, GPIO.LOW) #done
                GPIO.output(Motor1B, GPIO.HIGH) #done
                GPIO.output(Motor1E, GPIO.HIGH) #done

                GPIO.output(Motor2A, GPIO.HIGH) #done
                GPIO.output(Motor2B, GPIO.LOW) #done
                GPIO.output(Motor2E, GPIO.HIGH) #done

            if event.key == pygame.K_RIGHT:
                moving = "right"
                GPIO.output(Motor1A, GPIO.HIGH) #done
                GPIO.output(Motor1B, GPIO.LOW) #done
                GPIO.output(Motor1E, GPIO.HIGH) #done

                GPIO.output(Motor2A, GPIO.LOW) #done
                GPIO.output(Motor2B, GPIO.HIGH) #done
                GPIO.output(Motor2E, GPIO.HIGH) #done

            if event.key == pygame.K_UP:
                moving = "forward"
                GPIO.output(Motor1A, GPIO.LOW) #done
                GPIO.output(Motor1B, GPIO.HIGH) #done
                GPIO.output(Motor1E, GPIO.HIGH) #done

                GPIO.output(Motor2A, GPIO.LOW) #done
                GPIO.output(Motor2B, GPIO.HIGH) #done
                GPIO.output(Motor2E, GPIO.HIGH) #done

            if event.key == pygame.K_DOWN:
                GPIO.output(Motor1A, GPIO.HIGH) #done
                GPIO.output(Motor1B, GPIO.LOW) #done
                GPIO.output(Motor1E, GPIO.HIGH) #done

                GPIO.output(Motor2A, GPIO.HIGH) #done
                GPIO.output(Motor2B, GPIO.LOW) #done
                GPIO.output(Motor2E, GPIO.HIGH) #done
                moving = "backward"

            if event.key == pygame.K_c: #press C to quit
                done = True

        else:
            GPIO.output(Motor1E, GPIO.LOW)
            GPIO.output(Motor2E, GPIO.LOW)
            moving = "nothing"

    # run at 120 fps
    clock.tick(120)

GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
GPIO.cleanup()
pygame.quit()
