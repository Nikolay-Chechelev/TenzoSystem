from tkinter import *
import tkinter.font as font
from parameters import Parameters

import matplotlib.backends.backend_tkagg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as ani
from random import randint


# c = matplotlib.backends.backend_tkagg.FigureCanvasTk()

class MainWindow:
    def __init__(self, start_function=None, settings_window=None, parameters_window=None):
        self.start_function = start_function
        self.settings_window = settings_window
        self.parameters_window = parameters_window
        self.mainWindow = Tk()
        self.guiFont = font.Font(size=20)
        self.mainWindow.title('Процесс Тестирования - Cardina TenzoStand')
        self.mainWindow.configure(background='#333333',
                                  width=1100,
                                  height=700,
                                  )

        self.PrintButton = Button(self.mainWindow,
                                  text='ПЕЧАТЬ РЕЗУЛЬТАТОВ',
                                  font=self.guiFont,
                                  wraplength=250,
                                  background='#505050',
                                  foreground='#EEEEAA',
                                  activebackground='#656575',
                                  activeforeground='#9090E0',
                                  borderwidth=3,
                                  highlightbackground='#333333',
                                  relief='flat',
                                  height='10',
                                  width='30',
                                  command=self.start_button_cmd)
        self.PrintButton.place(relx=0,
                               rely=0,
                               relheight=0.2,
                               relwidth=0.25)

        self.TestSettingsButton = Button(self.mainWindow,
                                         text='НАСТРОЙКИ ТЕСТА',
                                         font=self.guiFont,
                                         wraplength=250,
                                         background='#505050',
                                         foreground='#EEEEAA',
                                         activebackground='#656575',
                                         activeforeground='#9090E0',
                                         borderwidth=3,
                                         highlightbackground='#333333',
                                         relief='flat',
                                         height='10',
                                         width='30',
                                         command=self.settings_button_cmd)
        self.TestSettingsButton.place(relx=0,
                                      rely=0.2,
                                      relheight=0.2,
                                      relwidth=0.25)

        self.ParameterSettingsButton = Button(self.mainWindow,
                                              text='ПАРАМЕТРЫ ОБОРУДОВАНИЯ',
                                              font=self.guiFont,
                                              wraplength=250,
                                              background='#505050',
                                              foreground='#EEEEAA',
                                              activebackground='#656575',
                                              activeforeground='#9090E0',
                                              borderwidth=3,
                                              highlightbackground='#333333',
                                              relief='flat',
                                              height='10',
                                              width='30',
                                              command=self.parameters_button_cmd)
        self.ParameterSettingsButton.place(relx=0,
                                           rely=0.4,
                                           relheight=0.2,
                                           relwidth=0.25)

        self.QualityChart = Canvas(self.mainWindow,
                                   width=600,
                                   height=600,
                                   background='#a0a0a0',
                                   highlightbackground='#909090',
                                   borderwidth=2,
                                   relief='groove',
                                   )
        self.QualityChart.place(relx=0.25,
                                rely=0,
                                relheight=0.6,
                                relwidth=0.75)

        self.StartTestButton = Button(self.mainWindow,
                                      text='START',
                                      font=self.guiFont,
                                      background='#506050',
                                      foreground='#EEEE55',
                                      activebackground='#657565',
                                      activeforeground='#9090E0',
                                      borderwidth=3,
                                      highlightbackground='#333333',
                                      relief='flat',
                                      height='10',
                                      width='30',
                                      command=self.start_button_cmd)
        self.StartTestButton.place(relx=0,
                                   rely=0.6,
                                   relheight=0.4,
                                   relwidth=0.25)

        self.LiveChart = Canvas(self.mainWindow,
                                width=900,
                                height=500,
                                background='#a0a0a0',
                                highlightbackground='#909090',
                                borderwidth=2,
                                relief='groove',
                                )
        self.LiveChart.place(relx=0.25,
                             rely=0.6,
                             relheight=0.4,
                             relwidth=0.75)
        # self.Quality = PlotChart(self.QualityChart, 'Динимические Параметры Амортизатора')
        # self.Live = PlotChart(self.LiveChart, 'Силовые Параметры Амортизатора')
        self.Quality = Chart(self.QualityChart, 'Динамические Параметры Амортизатора', 50, 50, 810, 350, 20, -50)
        self.Quality.print_coordinates()
        self.Live = Chart(self.LiveChart, 'Силовые Параметры Амортизатора', 50, 50, 810, 250, 20, 0)
        self.Live.print_coordinates()

    def start_button_cmd(self):
        m = self.start_function()
        self.Quality.draw_data([m[0], m[2], m[4]], [m[1], m[3], m[5]])

    def settings_button_cmd(self):
        self.settings_window().run()

    def parameters_button_cmd(self):
        self.parameters_window().run()

    def run(self):
        self.mainWindow.mainloop()


class Chart:
    def __init__(self, master, name, x1, y1, x2, y2, cell, zero_offset):
        self.name = name
        self.master = master
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cell = cell
        self.offset = zero_offset
        self.data_array = []
        self.axis_array = []
        self.font = ("colonna", 14, 'bold')
        self.font2 = ("colonna", 10)

    def print_coordinates(self):
        self.master.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='#FFFFFF', width=2)
        for x in range(self.x1, self.x2, self.cell):
            self.master.create_line(x, self.y1, x, self.y2, fill='#CCCCCC')
        for y in range(self.y1, self.y2, self.cell):
            self.master.create_line(self.x1, y, self.x2, y, fill='#CCCCCC')
        self.master.create_line((self.x2 + self.x1) // 2, self.y1, (self.x2 + self.x1) // 2, self.y2, fill='#999999',
                                width=2)
        self.master.create_line(self.x1, (self.y2 + self.y1) // 2 - self.offset, self.x2,
                                (self.y2 + self.y1) // 2 - self.offset, fill='#CCCCCC')
        self.master.create_text((self.x2 + self.x1) // 2, self.y1 // 2, text="Динамические Параметры Амортизатора",
                                font=self.font, fill="#303030")

    def draw_data(self, data_array, axis_array):
        self.data_array = data_array
        self.axis_array = axis_array
        min_load = []
        max_load = []
        for i in range(len(self.data_array)):
            min_load.append(min(self.data_array[i]))
            max_load.append(max(self.data_array[i]))
        print(min_load, max_load)
        y_min = round(min(min_load))
        y_max = round(max(max_load))
        y_step = round((y_max - y_min) / 14)
        m = 0
        i = 0
        while m < y_max:
            m += y_step
            i += 1
        self.offset = self.cell * (i - 7.5)
        self.master.create_line(self.x1, (self.y2 + self.y1) // 2 - self.offset, self.x2,
                                (self.y2 + self.y1) // 2 - self.offset, fill='#999999', width=2)
        x_ax = -180
        for x in range(self.x1 + self.cell, self.x2, self.cell * 2):
            self.master.create_text(x, (self.y2 + self.y1) // 2 + 10 - self.offset, text=str(x_ax), font=self.font2,
                                    fill="#303030")
            x_ax += 20

        kx = []
        ky = self.cell / y_step
        color = ['#A07070', '#70A070', '#7070A0']
        for i in range(len(self.data_array)):
            kx.append(4.05 * 360 / len(self.axis_array[i]))
            for j in range(len(self.data_array[i]) - 1):
                self.master.create_line((self.x2 + self.x1) // 2 + self.axis_array[i][j] * kx[i] + 5,
                                        (self.y2 + self.y1) // 2 - self.offset + self.data_array[i][j] * ky,
                                        (self.x2 + self.x1) // 2 + self.axis_array[i][j + 1] * kx[i] + 5,
                                        (self.y2 + self.y1) // 2 - self.offset + self.data_array[i][j + 1] * ky,
                                        fill=color[i], width=3)
        y = self.y2
        while y > self.y1:
            self.master.create_text(self.x1 - 20, y, text=str(-m), font=self.font2, fill="#303030")
            m -= y_step
            y -= self.cell
        return False


class TestSettingsWindow:
    def __init__(self):
        self.parameters = Parameters()
        self.parameters.read_parameters()
        print(self.parameters.parameters)
        self.settingsWindow = Tk()
        self.guiFont = font.Font(size=10)
        self.settingsWindow.title('Настройки Теста - Cardina TenzoStand')
        self.settingsWindow.configure(background='#333333',
                                      width=1100,
                                      height=600,
                                      )
        self.linear_speed_1 = StringVar()
        self.compress_load_1 = StringVar()
        self.rebound_load_1 = StringVar()

        self.linear_speed_2 = StringVar()
        self.compress_load_2 = StringVar()
        self.rebound_load_2 = StringVar()

        self.linear_speed_3 = StringVar()
        self.compress_load_3 = StringVar()
        self.rebound_load_3 = StringVar()

        self.start_id = StringVar()
        self.measurement_tolerance = StringVar()
        self.stand_name = StringVar()

        Label(master=self.settingsWindow,
              text="Параметры ПЕРВОГО Цикла Тестов",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0,
                      rely=0,
                      relwidth=0.5,
                      relheight=0.05)
        Label(master=self.settingsWindow,
              text='Линейная Скорость 1 (м/с)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.05,
                      relwidth=0.25,
                      relheight=0.05)
        self.ls1 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.linear_speed_1,
                         )
        self.ls1.place(relx=0.25,
                       rely=0.05,
                       relwidth=0.25,
                       relheight=0.05)
        self.ls1.insert(0, self.parameters.parameters['linear_speed_1'])
        Label(master=self.settingsWindow,
              text='Нагрузка на Сжатие 1 (кг)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.1,
                      relwidth=0.25,
                      relheight=0.05)
        self.cl1 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.compress_load_1,
                         )
        self.cl1.place(relx=0.25,
                       rely=0.1,
                       relwidth=0.25,
                       relheight=0.05)
        self.cl1.insert(0, self.parameters.parameters['compress_load_1'])
        Label(master=self.settingsWindow,
              text='Нагрузка на Отбой 1 (кг)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.15,
                      relwidth=0.25,
                      relheight=0.05)
        self.rl1 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.rebound_load_1,
                         )
        self.rl1.place(relx=0.25,
                       rely=0.15,
                       relwidth=0.25,
                       relheight=0.05)
        self.rl1.insert(0, self.parameters.parameters['rebound_load_1'])

        Label(master=self.settingsWindow,
              text="Параметры ВТОРОГО Цикла Тестов",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0,
                      rely=0.2,
                      relwidth=0.5,
                      relheight=0.05)
        Label(master=self.settingsWindow,
              text='Линейная Скорость 2 (м/с)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.25,
                      relwidth=0.25,
                      relheight=0.05)
        self.ls2 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.linear_speed_2,
                         )
        self.ls2.place(relx=0.25,
                       rely=0.25,
                       relwidth=0.25,
                       relheight=0.05)
        self.ls2.insert(0, self.parameters.parameters['linear_speed_2'])
        Label(master=self.settingsWindow,
              text='Нагрузка на Сжатие 2 (кг)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.3,
                      relwidth=0.25,
                      relheight=0.05)
        self.cl2 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.compress_load_2,
                         )
        self.cl2.place(relx=0.25,
                       rely=0.3,
                       relwidth=0.25,
                       relheight=0.05)
        self.cl2.insert(0, self.parameters.parameters['compress_load_2'])
        Label(master=self.settingsWindow,
              text='Нагрузка на Отбой 2 (кг)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.35,
                      relwidth=0.25,
                      relheight=0.05)
        self.rl2 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.rebound_load_2,
                         )
        self.rl2.place(relx=0.25,
                       rely=0.35,
                       relwidth=0.25,
                       relheight=0.05)
        self.rl2.insert(0, self.parameters.parameters['rebound_load_2'])

        Label(master=self.settingsWindow,
              text="Параметры ТРЕТЬЕГО Цикла Тестов",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0,
                      rely=0.4,
                      relwidth=0.5,
                      relheight=0.05)
        Label(master=self.settingsWindow,
              text='Линейная Скорость 3 (м/с)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.45,
                      relwidth=0.25,
                      relheight=0.05)
        self.ls3 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.linear_speed_3,
                         )
        self.ls3.place(relx=0.25,
                       rely=0.45,
                       relwidth=0.25,
                       relheight=0.05)
        self.ls3.insert(0, self.parameters.parameters['linear_speed_3'])
        Label(master=self.settingsWindow,
              text='Нагрузка на Сжатие 3 (кг)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.5,
                      relwidth=0.25,
                      relheight=0.05)
        self.cl3 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.compress_load_3,
                         )
        self.cl3.place(relx=0.25,
                       rely=0.5,
                       relwidth=0.25,
                       relheight=0.05)
        self.cl3.insert(0, self.parameters.parameters['compress_load_3'])
        Label(master=self.settingsWindow,
              text='Нагрузка на Отбой 3 (кг)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.55,
                      relwidth=0.25,
                      relheight=0.05)
        self.rl3 = Entry(master=self.settingsWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.rebound_load_3,
                         )
        self.rl3.place(relx=0.25,
                       rely=0.55,
                       relwidth=0.25,
                       relheight=0.05)
        self.rl3.insert(0, self.parameters.parameters['rebound_load_3'])

        Label(master=self.settingsWindow,
              text="Общие Настройки Теста",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0.5,
                      rely=0,
                      relwidth=0.5,
                      relheight=0.05)
        Label(master=self.settingsWindow,
              text='Стартовый Номер Образца',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0.5,
                      rely=0.05,
                      relwidth=0.25,
                      relheight=0.05)
        self.st_id = Entry(master=self.settingsWindow,
                           font=self.guiFont,
                           justify='center',
                           background='#555555',
                           foreground='#EEEEAA',
                           textvariable=self.start_id,
                           )
        self.st_id.place(relx=0.75,
                         rely=0.05,
                         relwidth=0.20,
                         relheight=0.05)
        self.st_id.insert(0, self.parameters.parameters['start_id'])
        Label(master=self.settingsWindow,
              text='Имя Стенда',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0.5,
                      rely=0.1,
                      relwidth=0.25,
                      relheight=0.05)
        self.st_name = Entry(master=self.settingsWindow,
                             font=self.guiFont,
                             justify='center',
                             background='#555555',
                             foreground='#EEEEAA',
                             textvariable=self.stand_name,
                             )
        self.st_name.place(relx=0.75,
                           rely=0.1,
                           relwidth=0.20,
                           relheight=0.05)
        self.st_name.insert(0, self.parameters.parameters['stand_name'])
        Label(master=self.settingsWindow,
              text='Допуск Измерений (%)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0.5,
                      rely=0.15,
                      relwidth=0.25,
                      relheight=0.05)
        self.mes_tol = Entry(master=self.settingsWindow,
                             font=self.guiFont,
                             justify='center',
                             background='#555555',
                             foreground='#EEEEAA',
                             textvariable=self.measurement_tolerance,
                             )
        self.mes_tol.place(relx=0.75,
                           rely=0.15,
                           relwidth=0.20,
                           relheight=0.05)

        self.mes_tol.insert(0, self.parameters.parameters['measurement_tolerance'])

        Button(master=self.settingsWindow,
               text='СОХРАНИТЬ',
               font=self.guiFont,
               wraplength=250,
               background='#505050',
               foreground='#EEEEAA',
               activebackground='#656575',
               activeforeground='#9090E0',
               borderwidth=3,
               highlightbackground='#333333',
               relief='flat',
               height='10',
               width='30',
               command=self.save_button,
               ).place(relx=0.05,
                       rely=0.75,
                       relwidth=0.4,
                       relheight=0.2)
        Button(master=self.settingsWindow,
               text='ОТМЕНА',
               font=self.guiFont,
               wraplength=250,
               background='#505050',
               foreground='#EEEEAA',
               activebackground='#656575',
               activeforeground='#9090E0',
               borderwidth=3,
               highlightbackground='#333333',
               relief='flat',
               height='10',
               width='30',
               command=self.settingsWindow.destroy,
               ).place(relx=0.55,
                       rely=0.75,
                       relwidth=0.4,
                       relheight=0.2)

    def save_button(self):
        self.parameters.parameters['linear_speed_1'] = self.ls1.get()
        self.parameters.parameters['compress_load_1'] = self.cl1.get()
        self.parameters.parameters['rebound_load_1'] = self.rl1.get()

        self.parameters.parameters['linear_speed_2'] = self.ls2.get()
        self.parameters.parameters['compress_load_2'] = self.cl2.get()
        self.parameters.parameters['rebound_load_2'] = self.rl2.get()

        self.parameters.parameters['linear_speed_3'] = self.ls3.get()
        self.parameters.parameters['compress_load_3'] = self.cl3.get()
        self.parameters.parameters['rebound_load_3'] = self.rl3.get()

        self.parameters.parameters['start_id'] = self.st_id.get()
        self.parameters.parameters['stand_name'] = self.st_name.get()
        self.parameters.parameters['measurement_tolerance'] = self.mes_tol.get()
        self.parameters.save_parameters()
        self.settingsWindow.destroy()

    def run(self):
        self.settingsWindow.mainloop()


class ParameterSettingsWindow:
    def __init__(self):
        self.parametersWindow = Tk()
        self.guiFont = font.Font(size=20)
        self.parametersWindow.title('Параметры Оборудования - Cardina TenzoStand')
        self.parameters = Parameters()
        self.parameters.read_parameters()
        print(self.parameters.parameters)

        self.drive_power = StringVar()
        self.max_load = StringVar()
        self.max_freq = StringVar()
        self.radius = StringVar()
        self.gear_ratio = StringVar()
        self.drive_speed = StringVar()
        self.rkp = StringVar()
        self.sensor_voltage = StringVar()

        self.parametersWindow.configure(background='#333333',
                                        width=1100,
                                        height=600,
                                        )
        Label(master=self.parametersWindow,
              text="Параметры Установленного оборудования",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0,
                      rely=0,
                      relwidth=0.5,
                      relheight=0.05)
        Label(master=self.parametersWindow,
              text='Мощность Двигателя (Вт)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.05,
                      relwidth=0.25,
                      relheight=0.05)
        self.drv_pow = Entry(master=self.parametersWindow,
                             font=self.guiFont,
                             justify='center',
                             background='#555555',
                             foreground='#EEEEAA',
                             textvariable=self.drive_power,
                             )
        self.drv_pow.place(relx=0.25,
                           rely=0.05,
                           relwidth=0.25,
                           relheight=0.05)
        self.drv_pow.insert(0, self.parameters.parameters['drive_power'])

        Label(master=self.parametersWindow,
              text='Максимальная Нагрузка (кг)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.1,
                      relwidth=0.25,
                      relheight=0.05)
        self.max_ld = Entry(master=self.parametersWindow,
                            font=self.guiFont,
                            justify='center',
                            background='#555555',
                            foreground='#EEEEAA',
                            textvariable=self.max_load,
                            )
        self.max_ld.place(relx=0.25,
                          rely=0.1,
                          relwidth=0.25,
                          relheight=0.05)
        self.max_ld.insert(0, self.parameters.parameters['max_load'])

        Label(master=self.parametersWindow,
              text='Максимальная Частота (Гц)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.15,
                      relwidth=0.25,
                      relheight=0.05)
        self.max_fr = Entry(master=self.parametersWindow,
                            font=self.guiFont,
                            justify='center',
                            background='#555555',
                            foreground='#EEEEAA',
                            textvariable=self.max_freq,
                            )
        self.max_fr.place(relx=0.25,
                          rely=0.15,
                          relwidth=0.25,
                          relheight=0.05)
        self.max_fr.insert(0, self.parameters.parameters['max_freq'])

        Label(master=self.parametersWindow,
              text='Радиус Вращения Колена (м)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.2,
                      relwidth=0.25,
                      relheight=0.05)
        self.rad = Entry(master=self.parametersWindow,
                         font=self.guiFont,
                         justify='center',
                         background='#555555',
                         foreground='#EEEEAA',
                         textvariable=self.radius,
                         )
        self.rad.place(relx=0.25,
                       rely=0.2,
                       relwidth=0.25,
                       relheight=0.05)
        self.rad.insert(0, self.parameters.parameters['radius'])

        Label(master=self.parametersWindow,
              text='Передаточное Число Редуктора',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.25,
                      relwidth=0.25,
                      relheight=0.05)
        self.gr_rat = Entry(master=self.parametersWindow,
                            font=self.guiFont,
                            justify='center',
                            background='#555555',
                            foreground='#EEEEAA',
                            textvariable=self.gear_ratio,
                            )
        self.gr_rat.place(relx=0.25,
                          rely=0.25,
                          relwidth=0.25,
                          relheight=0.05)
        self.gr_rat.insert(0, self.parameters.parameters['gear_ratio'])

        Label(master=self.parametersWindow,
              text='Обороты Двигателя (об/мин)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.3,
                      relwidth=0.25,
                      relheight=0.05)
        self.drv_spd = Entry(master=self.parametersWindow,
                            font=self.guiFont,
                            justify='center',
                            background='#555555',
                            foreground='#EEEEAA',
                            textvariable=self.drive_speed,
                            )
        self.drv_spd.place(relx=0.25,
                          rely=0.3,
                          relwidth=0.25,
                          relheight=0.05)
        self.drv_spd.insert(0, self.parameters.parameters['drive_speed'])

        Label(master=self.parametersWindow,
              text='РКП Тензодатчика (мВ/В)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.35,
                      relwidth=0.25,
                      relheight=0.05)
        self.rkp_tz = Entry(master=self.parametersWindow,
                             font=self.guiFont,
                             justify='center',
                             background='#555555',
                             foreground='#EEEEAA',
                             textvariable=self.rkp,
                             )
        self.rkp_tz.place(relx=0.25,
                           rely=0.35,
                           relwidth=0.25,
                           relheight=0.05)
        self.rkp_tz.insert(0, self.parameters.parameters['rkp'])

        Label(master=self.parametersWindow,
              text='Напряжение Тензодатчика (В)',
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEEAA',
              ).place(relx=0,
                      rely=0.4,
                      relwidth=0.25,
                      relheight=0.05)
        self.v_tz = Entry(master=self.parametersWindow,
                            font=self.guiFont,
                            justify='center',
                            background='#555555',
                            foreground='#EEEEAA',
                            textvariable=self.sensor_voltage,
                            )
        self.v_tz.place(relx=0.25,
                          rely=0.4,
                          relwidth=0.25,
                          relheight=0.05)
        self.v_tz.insert(0, self.parameters.parameters['sensor_voltage'])

        Button(master=self.parametersWindow,
               text='СОХРАНИТЬ',
               font=self.guiFont,
               wraplength=250,
               background='#505050',
               foreground='#EEEEAA',
               activebackground='#656575',
               activeforeground='#9090E0',
               borderwidth=3,
               highlightbackground='#333333',
               relief='flat',
               height='10',
               width='30',
               command=self.save_button,
               ).place(relx=0.05,
                       rely=0.75,
                       relwidth=0.4,
                       relheight=0.2)
        Button(master=self.parametersWindow,
               text='ОТМЕНА',
               font=self.guiFont,
               wraplength=250,
               background='#505050',
               foreground='#EEEEAA',
               activebackground='#656575',
               activeforeground='#9090E0',
               borderwidth=3,
               highlightbackground='#333333',
               relief='flat',
               height='10',
               width='30',
               command=self.parametersWindow.destroy,  # TODO Дописать процедуру сохранения параметров
               ).place(relx=0.55,
                       rely=0.75,
                       relwidth=0.4,
                       relheight=0.2)

    def save_button(self):
        self.parameters.parameters['drive_power'] = self.drv_pow.get()
        self.parameters.parameters['max_load'] = self.max_ld.get()
        self.parameters.parameters['max_freq'] = self.max_fr.get()
        self.parameters.parameters['radius'] = self.rad.get()
        self.parameters.parameters['gear_ratio'] = self.gr_rat.get()
        self.parameters.parameters['drive_speed'] = self.drv_spd.get()
        self.parameters.parameters['rkp'] = self.rkp_tz.get()
        self.parameters.parameters['sensor_voltage'] = self.v_tz.get()
        self.parameters.save_parameters()
        self.parametersWindow.destroy()
        return 0

    def run(self):
        self.parametersWindow.mainloop()


# TODO Нерабочий класс. Нужно добиться запуска на Распберри
class PlotChart:
    def __init__(self, master, name, func=None):
        self.master = master
        self.name = name
        self.chart_data = None
        self.figure = plt.Figure(figsize=(100, 100), dpi=100)
        self.chart_type = FigureCanvasTkAgg(self.figure, self.master)
        self.figure.patch.set_facecolor('#A0A0A0')
        self.chart = self.figure.add_subplot(111)
        self.chart.set_title(self.name)
        self.chart.axhline(color='black', lw=1.5)
        self.chart.axvline(color='black', lw=1.5)
        self.chart.grid()
        self.chart.plot()
        self.chart_type.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)

    def plot(self, char_data1, axis_data1, char_data2, axis_data2):
        self.__init__(self.master, self.name)
        self.chart.plot(axis_data1, char_data1)
        self.chart.plot(axis_data2, char_data2)
        self.chart_type.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)

    def place(self):
        pass

# s = TestSettingsWindow()
# s.run()
