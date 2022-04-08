import csv,  sys
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
# data = lpf.LPF(data)
# data = lpf.LPF(data)
# data = lpf.LPF(data)
index_p = []
index_n = []
cross = 0

for i in range(len(data) - 1):
    if data[i] * data[i+1] < 0:
        index_p.append(cross + (i - cross) // 2)
        cross = i

plt.plot(data)
plt.show()

display = pygame.display
screen = display.set_mode([1000, 1000])
done = None
x = 500
y = -1
m = -1
t = (max(data) + min(data)) // 2
t = -11.5
print(t, max(data), min(data))
for i in range(len(data)):
    pygame.draw.line(screen, [100, 100, 100], [x, data[i]*5 + 500], [x, data[i + 1]*5 + 500])
    pygame.draw.line(screen, [100, 0, 100], [i, data[i]*5 + 500], [i + 1, data[i + 1]*5 + 500])
    print(i)
    # if i in index_p:
    #     print('p', i)
    #     y *= -1
    # if (data[i] * data[i+1]) < 0:
    #     m *= -1
    # x += m
    if data[i] > t:
        x += 1
    else:
        x -= 1


    display.flip()
    sleep(0.001)
    # screen.fill([0, 0, 0])
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
