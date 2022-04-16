from GUI import *

class main:
    def __init__(self):
        self.settings_window = TestSettingsWindow
        self.parameters_window = ParameterSettingsWindow
        self.main_window = MainWindow(self.start_test, self.settings_window, self.parameters_window)
        self.main_window.run()

    def start_test(self):
        pass




m = main()
