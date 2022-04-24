'''import serial,  sys
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
'''
import pygame
from tenzo import tenzo as tnz
import time
from time import sleep
import threading
import sys
from random import randint

class pygame_charts:
    def __init__(self, tenzo_sensor):
        self.width = 1000
        self.height = 500
        self.display = pygame.display
        self.screen = self.display.set_mode([self.width, self.height])
        self.done = False
        self.tenzo_sensor = tenzo_sensor()
        self.tenzo_data = [0] * self.width
        n = randint(0, 1000000)
        self.f = open('samples/test_with_gui.csv'.format(n), 'w')
        data_thread = threading.Thread(target=self.collect_data, args=(self.done, ))
        data_thread.start()
        pass
    
    def collect_data(self, done):
        while not self.done:
            del self.tenzo_data[0]
            a = self.tenzo_sensor.get_weight()
            self.tenzo_data.append(a)
            self.f.write(str(a).replace('.', ',') + ';\r\n')
            sleep(0.001)
    
    def mainloop(self):
        k = 5
        while not self.done:
            self.screen.fill([0, 0, 0])
            for i in range(len(self.tenzo_data) - 1):
                # pygame.draw.line(self.screen, [255, 100, 100], [i, 350 - data[i]], [i+1, 350 - data[i + 1]], 1)
                pygame.draw.line(self.screen, [255, 100, 255], [i, self.height/2 - self.tenzo_data[i]*k], [i + 1, self.height/2 - self.tenzo_data[i + 1]*k], 1)
            pygame.draw.line(self.screen, [0, 100, 100], [0, self.height/2], [self.width, self.height/2])
            self.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
p = pygame_charts(tnz)
p.mainloop()
