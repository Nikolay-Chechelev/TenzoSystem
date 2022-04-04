import csv
from DSP import DSP
from matplotlib import pyplot as plt
from time import sleep
import pygame

f = open('samples/f_sample_933338.csv', 'r')

csv_data = csv.reader(f, delimiter=';')
data = []
for row in csv_data:
    data.append(float(row[0].replace(',', '.')))

plt.plot(data)

lpf = DSP(500)
lpf.init_lp_filter(1)
data = lpf.LPF(data)
data = lpf.LPF(data)
data = lpf.LPF(data)
data = lpf.LPF(data)

plt.plot(data)
plt.show()

display = pygame.display
screen = display.set_mode([1000, 1000])
done = None
y = 500
for i in range(1500):
    if data[i] > 0:
        pygame.draw.line(screen, [100, 100, 100], [y, data[i]*10 + 500], [y + 3, data[i + 1]*10 + 500])
        y += 3
    if data[i] <= 0:
        pygame.draw.line(screen, [100, 100, 100], [y, data[i]*5 + 500], [y - 2, data[i + 1]*5 + 500])
        y -= 2
    display.flip()
    sleep(0.01)
while not done:

    if pygame.event.get() == pygame.QUIT:
        pygame.quit()