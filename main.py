from GUI import *
from data_processing import GetData, LoadCharts
# from test_flow import TestFlow
from parameters import Parameters

class main:
    def __init__(self):
        # self.test = TestFlow()
        self.parameters = Parameters()
        self.parameters.read_parameters()
        self.sample_id = int(self.parameters.parameters['start_id'])
        self.settings_window = TestSettingsWindow
        self.parameters_window = ParameterSettingsWindow
        self.main_window = MainWindow(self.start_test, self.settings_window, self.parameters_window)
        self.main_window.run()

    def start_test(self):
        self.sample_id += 1

        # data = self.test.run()
        #
        # a = LoadCharts(data[0])
        # dt1, ax1 = a.get_load_charts()
        # a = LoadCharts(data[1])
        # dt2, ax2 = a.get_load_charts()
        # a = LoadCharts(data[2])
        # dt3, ax3 = a.get_load_charts()
        # print(dt1, ax1, dt2, ax2, dt3, ax3)
        # print(len(dt1), len(ax1), len(dt2), len(ax2), len(dt3), len(ax3))

        a = GetData('samples_new/nerab_50.csv')
        data = a.read()
        dt1, ax1 = LoadCharts(data).get_load_charts()
        a = GetData('samples_new/nerab_140.csv')
        data = a.read()
        dt2, ax2 = LoadCharts(data).get_load_charts()
        a = GetData('samples_new/rab_50.csv')
        data = a.read()
        dt3, ax3 = LoadCharts(data).get_load_charts()
        self.parameters.parameters['start_id'] = self.sample_id
        self.parameters.save_parameters()
        return dt1, ax1, dt2, ax2, dt3, ax3


m = main()
