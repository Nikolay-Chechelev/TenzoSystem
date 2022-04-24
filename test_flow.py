# 1. Проверка периферийных устройств
#     Проверка АЦП на шине
#     ПРоверка ЦАП на шине
# 2. Считывание параметров и настроек
# 3. Запуск минимальной скорости для проверки лома
#     алгоритм контроля усилия по производной.
# 4. 10 прогонов на максимальной скорости длля разгона жидкости
#     Контроль хода по пересечению 0
# 5. Останов
# 6. Понижение до первой скорости. Начало записи от пересечения нуля
# 7. 5 прогонов на первой скорости.
# 8. Останов
# 9. Повышение до второй скорости
# 10. 5 прогонов на 2 сторости
# 11. Останов
# 12. Повышение до 3 скорости
# 13. 5 прогонов на 3 скорости
# 14. Останов
# 15. Преобразование данных
# 16. Анализ данных
# 17. Отрисовка графиков
from ADS1115 import ads1115
from MCP4725 import mcp4725
from tenzo import Tenzo
from parameters import Parameters
from time import sleep

class TestFlow:
    def __init__(self):
        self.adc = ads1115()
        self.dac = mcp4725()
        self.dac.set_voltage(0)
        sleep(5)
        self.tenzo = Tenzo()
        self.parameters = Parameters()
        self.first_cycle_data = []
        self.second_cycle_data = []
        self.third_cycle_data = []

    def i2c_bus_test(self):
        if self.adc.check_available():
            return True
        if self.dac.check_available():
            return True
        return False

    def load_settings(self):
        self.parameters.read_parameters()
        return False

    def set_freq(self, freq):
        f_max = int(self.parameters.parameters['max_freq'])
        voltage = freq * (10.0 / f_max)
        print('V = ', voltage)
        return self.dac.set_voltage(voltage)

    def stop_drive(self):
        return self.dac.set_voltage(0)

    def check_jamming(self):
        max_jamming_load = int(self.parameters.parameters['max_load'])
        self.set_freq(20.0)
        sleep(3)
        m = self.tenzo.get_weight()
        if m > max_jamming_load:
            self.stop_drive()
            print('ERROR')
            return True
        self.stop_drive()
        return False
        
    def first_cycle(self):
        sleep(1)
        self.set_freq(50.0) # TODO: Set freq from 
        sleep(1)
        i = 0
        m1 = self.tenzo.get_weight()
        sleep(0.001)
        m2 = self.tenzo.get_weight()
        while(m1 * m2) >= 0:
            m1 = m2
            m2 = self.tenzo.get_weight()
            sleep(0.001)
            
        while(i <= 30):
            m2 = self.tenzo.get_weight()
            if (m1 * m2) < 0:
                i += 1
            m1 = m2
            self.first_cycle_data.append(m2)
            sleep(0.001)
        self.stop_drive()
        print(len(self.first_cycle_data))
        return False
    
    def second_cycle(self):
        sleep(1)
        self.set_freq(90.0) # TODO: Set freq from 
        sleep(1)
        i = 0
        m1 = self.tenzo.get_weight()
        sleep(0.001)
        m2 = self.tenzo.get_weight()
        while(m1 * m2) >= 0:
            m1 = m2
            m2 = self.tenzo.get_weight()
            sleep(0.001)
            
        while(i <= 30):
            m2 = self.tenzo.get_weight()
            if (m1 * m2) < 0:
                i += 1
            m1 = m2
            self.second_cycle_data.append(m2)
            sleep(0.001)
        self.stop_drive()
        print(len(self.second_cycle_data))
        return False
    
    def third_cycle(self):
        sleep(1)
        self.set_freq(130.0) # TODO: Set freq from 
        sleep(1)
        i = 0
        m1 = self.tenzo.get_weight()
        sleep(0.001)
        m2 = self.tenzo.get_weight()
        while(m1 * m2) >= 0:
            m1 = m2
            m2 = self.tenzo.get_weight()
            sleep(0.001)
            
        while(i <= 30):
            m2 = self.tenzo.get_weight()
            if (m1 * m2) < 0:
                i += 1
            m1 = m2
            self.third_cycle_data.append(m2)
            sleep(0.001)
        self.stop_drive()
        print(len(self.third_cycle_data))
        return False
        
        

    def run(self):
        if self.i2c_bus_test():
            return 'Ошибка инициализации периферии...'
        self.load_settings()
        if self.check_jamming():
            return "Недопустимые нагрузки на стенд..."
        self.first_cycle()
        self.second_cycle()
        self.third_cycle()

        return self.first_cycle_data, self.second_cycle_data, self.third_cycle_data

#a = TestFlow()
#a.run()
