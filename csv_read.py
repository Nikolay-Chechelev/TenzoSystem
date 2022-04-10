import csv, sys
from DSP import DSP
from matplotlib import pyplot as plt
from time import sleep
import pygame

f = open('samples/zavod_nerab_10_938155.csv', 'r')

csv_data = csv.reader(f, delimiter=';')
data = []
for row in csv_data:
    data.append(float(row[0].replace(',', '.')))

plt.plot(data)

lpf = DSP(500)
lpf.init_lp_filter(1)
data = lpf.LPF(data)
data = lpf.increase_sample_array(data)

plt.plot(data)
plt.show()

display = pygame.display
screen = display.set_mode([1000, 1000])
done = None
x = 500
c = 1.5
pygame.draw.line(screen, [100, 0, 100], [500, 0], [500, 1000], 3)
display.flip()
for i in range(len(data) - 2):
    if data[i + 1] * data[i] < 0:
        c *= -1
    sleep(0.0001)
    pygame.draw.line(screen, [100, 100, 100], [-data[i] * 10 + 500, x, ], [-data[i + 1] * 10 + 500, x + c, ])
    x += c
    display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
