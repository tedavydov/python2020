import time


class TrafficLight:
    __color = ["красный", "желтый", "зеленый", "желтый"]
    __term_color = ["\033[31m", "\033[33m", "\033[32m", "\033[31m\033[43m"]
    __color_time = [7, 2, 5, 2]

    def __init__(self, time=None):
        if time and isinstance(time, int):
            self.time_full = time
            self.timing_flag = True
        else:
            self.time_full = 20
            self.timing_flag = False

    def running(self, color=None):
        self.time_start = int(time.perf_counter())
        self.time_curr = self.time_start
        self.__color_run(color)
        while self.time_full > (self.time_curr - self.time_start):
            self.__color_run(0)
            self.time_curr = int(time.perf_counter())
        if self.timing_flag:
            print("STOP" + f"{'time = ':>15}" + f"{str(int(time.perf_counter())):>4}")
        else:
            print("STOP")

    def __color_run(self, col):
        col_num = 0
        if col:
            if isinstance(col, str):
                if col in self.__color:
                    col_num = self.__color.index(col)
            elif isinstance(col, int):
                if col >= 0 and col <= 2:
                    col_num = col
            else:
                print("Вы ошиблись, у светофора нет такого цвета")

        for i in range(len(self.__color)):
            if i >= col_num:
                self.time_curr = int(time.perf_counter())
                if self.time_full <= (self.time_curr - self.time_start):
                    break
                else:
                    if self.timing_flag:
                        print(self.__term_color[i] + f"{self.__color[i]:<11}"
                              + "\033[0m" + f" time = {str(int(time.perf_counter())):>4}")
                    else:
                        print(self.__term_color[i] + f"{self.__color[i]:<11}" + "\033[0m")
                    time.sleep(self.__color_time[i])


# a = TrafficLight()   # запуск на стандартное время около 20 сек
a = TrafficLight(13)   # запуск с заданным временем работы

# a.running("жел")     # начать с цвета (цвет задан ошибочно)
# a.running("желтый")  # начать с цвета (цвет задан текстом)
a.running(1)           # начать с цвета (цвет задан числом от 0 до 2)
# a.running()          # стандартный запуск
