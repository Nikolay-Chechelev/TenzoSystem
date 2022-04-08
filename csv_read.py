import csv,  sys
from DSP import DSP
from matplotlib import pyplot as plt
from time import sleep
import pygame

f = open('samples/Good_amort_50hz.csv', 'r')

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

def fix_array(array):
    l1 = 0
    l2 = 0
    x = 0
    i = 0
    d = 0

    while array[i] * array[i + 1] >= 0 and x == 0:
        i += 1
    x = i - x
    i += 1

    while i < len(array)-5000:
        x = i
        i += 1
        while array[i] * array[i + 1] >= 0:
            i += 1
        l1 = i - x
        x = i
        i += 1
        print('1 halfperiod =', l1)

        while array[i] * array[i + 1] >= 0:
            i += 1
        l2 = i - x
        print('2 halfperiod =', l2)

        if l1 == l2:
            pass
        if l1 > l2:
            d = l1 // (l1 - l2)
            m = l1 - l2
            while m > 0:
                del array[i - l1 + d * m]
                m -= 1
            i -= l1 - l2

        if l1 < l2:
            d = l2 // (l2 - l1)
            m = l2 - l1
            while m > 0:
                del array[i - l2 + d * m]
                m -= 1
            i -= l2 - l1
        sleep(0.1)
    return array

data = fix_array(data)
plt.plot(data)
plt.show()

display = pygame.display
screen = display.set_mode([1000, 1000])
done = None
x = 500
c = 1
for i in range(len(data) - 2):
    pygame.draw.line(screen, [100, 100, 100], [x, data[i]*5 + 500], [x, data[i + 1]*5 + 500])
    pygame.draw.line(screen, [100, 0, 100], [i, data[i]*5 + 500], [i + 1, data[i + 1]*5 + 500])
    if data[i+1] * data[i] < 0:
        c *= -1
    x += c



    display.flip()
    sleep(0.001)
    # screen.fill([0, 0, 0])
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
