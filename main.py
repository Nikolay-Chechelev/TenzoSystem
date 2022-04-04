import serial
import pygame
from random import randint
import DSP
display = pygame.display
screen = display.set_mode([1500, 700])
port = serial.Serial('/dev/ttyACM0', '115200')
done = None
a = randint(0, 1000000)

f = open('samples/fo_sample_{}.csv'.format(a), 'w')
data = [0] * 1500

def get_weight():
    s = str(port.read(1))
    while s != '\r':
        s += str(port.read(1))


while not done:
    s = port.read(1).decode('utf-8')
    while not 'd' in s:
        s += port.read(1).decode('utf-8')
    s = eval(s.split('d')[0])
    print(s)
    f.write(str(s).replace('.', ',') + ';\r\n')
    data.append(s * 5)
    del data[0]
    screen.fill([0, 0, 0])
    for i in range(len(data) - 1):
        pygame.draw.line(screen, [255, 100, 100], [i, 350 - data[i]], [i+1, 350 - data[i + 1]], 1)
    pygame.draw.line(screen, [0, 100, 100], [0, 350], [1500, 350])
    display.flip()

    if pygame.event.get() == pygame.QUIT:
        pygame.quit()