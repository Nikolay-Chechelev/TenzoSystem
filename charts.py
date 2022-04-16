import serial,  sys
import pygame
from random import randint
from DSP import DSP
display = pygame.display
screen = display.set_mode([1500, 700])
port = serial.Serial('/dev/ttyACM0', '115200')
done = None
a = randint(0, 1000000)
print(a)
f = open('samples/zavod_nerab_10_{}.csv'.format(a), 'w')
data_raw = [0] * 1500
data = [0] * 1500

def get_weight():
    s = str(port.read(1))
    while s != '\r':
        s += str(port.read(1))
lpf = DSP(500)
lpf.init_lp_filter(1)

while not done:
    s = port.read(1).decode('utf-8')
    while not 'd' in s:
        s += port.read(1).decode('utf-8')
    s = eval(s.split('d')[0])
    print(s)
    f.write(str(s).replace('.', ',') + ';\r\n')
    data.append(s * 5)
    del data[0]

    data_raw = lpf.LPF(data)
    # data_raw = lpf.LPF(data_raw)
    # data_raw = lpf.LPF(data_raw)
    # data_raw = lpf.LPF(data_raw)
    
    screen.fill([0, 0, 0])
    for i in range(len(data) - 1):
        # pygame.draw.line(screen, [255, 100, 100], [i, 350 - data[i]], [i+1, 350 - data[i + 1]], 1)
        pygame.draw.line(screen, [255, 100, 255], [i, 350 - data_raw[i]], [i + 1, 350 - data_raw[i + 1]], 1)
    pygame.draw.line(screen, [0, 100, 100], [0, 350], [1500, 350])
    display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

