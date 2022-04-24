from DSP import DSP
import csv
from matplotlib import pyplot as plt

class LoadCharts:
    def __init__(self, data_array, linear_speed=100):
        self.dsp = DSP(10)
        self.dsp.init_lp_filter(1)
        self.part = []
        self.parted_data = []
        self.mins = []
        self.maxs = []
        self.abscissa_len = 100
        self.abscissa = []
        self.data = data_array
        self.separate_data()
        self.correct_sinus()
        self.get_abscissa()
        self.average_data = [0] * 2 * self.abscissa_len
        pass

    def separate_data(self):
        self.data = self.dsp.LPF(self.data)
        m = 0
        for i in range(1, len(self.data)):
            if self.data[i - 1] * self.data[i] < 0:
                if len(self.part) > 10:
                    self.parted_data.append(self.part)
                self.part = []
                m += 1
            self.part.append(self.data[i])
        self.abscissa_len = len(self.data) // m
        if self.abscissa_len % 2 != 0:
            self.abscissa_len -= 1
        return 0

    def correct_sinus(self):
        for i in range(len(self.parted_data)):
            sinus = []
            m = 0
            if self.parted_data[i][len(self.parted_data)//2] > 0:
                m = max(self.parted_data[i])
            else:
                m = min(self.parted_data[i])
            sinus.append(self.parted_data[i][0:self.parted_data[i].index(m)])
            sinus.append(self.parted_data[i][self.parted_data[i].index(m):len(self.parted_data[i]) - 1])
            sinus[1] = self.dsp.correct_sample_rate(sinus[1], len(sinus[0]))
            self.parted_data[i] = sinus[0] + sinus[1]
        return 0


    def get_abscissa(self):
        for i in range(self.abscissa_len * 2):
            if i < self.abscissa_len:
                self.abscissa.append(i - self.abscissa_len // 2)
            if i >= self.abscissa_len:
                self.abscissa.append(self.abscissa_len - 1 - (i - self.abscissa_len // 2))
        self.abscissa.append(self.abscissa[0])
        return 0

    def get_load_charts(self):
        for i in range(len(self.parted_data)):
            self.parted_data[i] = self.dsp.correct_sample_rate(self.parted_data[i], self.abscissa_len)
            for j in range(self.abscissa_len):
                if i % 2 == 0:
                    self.average_data[j] += self.parted_data[i][j] / (len(self.parted_data) / 2)
                else:
                    self.average_data[j + self.abscissa_len] += self.parted_data[i][j] / (len(self.parted_data) / 2)
        self.average_data.append(self.average_data[0])
        return self.average_data, self.abscissa


class GetData:
    def __init__(self, file):
        self.f = open(file, 'r')
        self.csv_data = csv.reader(self.f, delimiter=';')
        self.data = []

    def read(self):
        for row in self.csv_data:
            self.data.append(float(row[0].replace(',', '.')))
        return self.data


# from matplotlib import pyplot as plt
#
# a = GetData('samples_new/nerab_140.csv')
# data = a.read()
# print(len(data))
# plt.plot(data)
# plt.show()
#
# d = DSP(2)
# data = d.correct_sample_rate(data, len(data) * 5)
# plt.plot(data)
# plt.show()
# f = open('samples_new/nerab_50_sized.csv', 'w')
# for i in range(len(data)):
#     f.write(str(data[i]).replace('.', ',') + ';\r\n')
# l = LoadCharts(data)