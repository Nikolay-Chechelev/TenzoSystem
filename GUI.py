from tkinter import *
import tkinter.font as font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
                                  height=600,
                                  )
        self.StartTestButton = Button(self.mainWindow,
                                      text='START',
                                      font=self.guiFont,
                                      background='#505050',
                                      foreground='#EEEE55',
                                      activebackground='#656575',
                                      activeforeground='#9090E0',
                                      borderwidth=3,
                                      highlightbackground='#333333',
                                      relief='flat',
                                      height='10',
                                      width='30',
                                      command=self.start_button_cmd)
        self.StartTestButton.place(relx=0,
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

        self.LiveChart = Canvas(self.mainWindow,
                                width=900,
                                height=500,
                                background='#a0a0a0',
                                highlightbackground='#909090',
                                borderwidth=2,
                                relief='groove',
                                )
        self.LiveChart.place(relx=0,
                             rely=0.6,
                             relheight=0.4,
                             relwidth=1)

    def start_button_cmd(self):
        pass

    def settings_button_cmd(self):
        self.settings_window().run()

    def parameters_button_cmd(self):
        self.parameters_window().run()

    def run(self):
        self.mainWindow.mainloop()


class TestSettingsWindow:
    def __init__(self):
        self.settingsWindow = Tk()
        self.guiFont = font.Font(size=10)
        self.settingsWindow.title('Настройки Теста - Cardina TenzoStand')
        self.settingsWindow.configure(background='#333333',
                                      width=1100,
                                      height=600,
                                      )
        #TODO Нужно инициализировать эти переменные из сохранненых параметров
        self.linear_speed_1 = IntVar()
        self.compress_load_1 = IntVar()
        self.rebound_load_1 = IntVar()

        self.linear_speed_2 = IntVar()
        self.compress_load_2 = IntVar()
        self.rebound_load_2 = IntVar()

        self.linear_speed_3 = IntVar()
        self.compress_load_3 = IntVar()
        self.rebound_load_3 = IntVar()

        Label(master=self.settingsWindow,
              text="Параметры ПЕРВОГО Цикла Тестов",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0,
                      rely=0,
                      relwidth=1,
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.linear_speed_1,
              ).place(relx=0.25,
                      rely=0.05,
                      relwidth=0.25,
                      relheight=0.05)
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.compress_load_1,
              ).place(relx=0.25,
                      rely=0.1,
                      relwidth=0.25,
                      relheight=0.05)
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.rebound_load_1,
              ).place(relx=0.25,
                      rely=0.15,
                      relwidth=0.25,
                      relheight=0.05)

        Label(master=self.settingsWindow,
              text="Параметры ВТОРОГО Цикла Тестов",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0,
                      rely=0.2,
                      relwidth=1,
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.linear_speed_2,
              ).place(relx=0.25,
                      rely=0.25,
                      relwidth=0.25,
                      relheight=0.05)
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.compress_load_2,
              ).place(relx=0.25,
                      rely=0.3,
                      relwidth=0.25,
                      relheight=0.05)
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.rebound_load_2,
              ).place(relx=0.25,
                      rely=0.35,
                      relwidth=0.25,
                      relheight=0.05)

        Label(master=self.settingsWindow,
              text="Параметры ТРЕТЬЕГО Цикла Тестов",
              font=self.guiFont,
              justify='center',
              background='#333333',
              foreground='#EEEE55',
              ).place(relx=0,
                      rely=0.4,
                      relwidth=1,
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.linear_speed_3,
              ).place(relx=0.25,
                      rely=0.45,
                      relwidth=0.25,
                      relheight=0.05)
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.compress_load_3,
              ).place(relx=0.25,
                      rely=0.5,
                      relwidth=0.25,
                      relheight=0.05)
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
        Entry(master=self.settingsWindow,
              font=self.guiFont,
              justify='center',
              background='#555555',
              foreground='#EEEEAA',
              textvariable=self.rebound_load_3,
              ).place(relx=0.25,
                      rely=0.55,
                      relwidth=0.25,
                      relheight=0.05)

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
               command=self.settingsWindow.destroy, #TODO Дописать процедуру сохранения параметров
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
               command=self.settingsWindow.destroy,  # TODO Дописать процедуру сохранения параметров
               ).place(relx=0.55,
                       rely=0.75,
                       relwidth=0.4,
                       relheight=0.2)

    def run(self):
        self.settingsWindow.mainloop()


class ParameterSettingsWindow:
    def __init__(self):
        self.parametersWindow = Tk()
        self.guiFont = font.Font(size=20)
        self.parametersWindow.title('Параметры Оборудования - Cardina TenzoStand')
        self.parametersWindow.configure(background='#333333',
                                        width=1100,
                                        height=600,
                                        )
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
               command=self.parametersWindow.destroy,  # TODO Дописать процедуру сохранения параметров
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


    def run(self):
        self.parametersWindow.mainloop()


# s = TestSettingsWindow()
# s.run()
