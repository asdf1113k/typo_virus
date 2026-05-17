import threading

from time import sleep


func1 = lambda: print(["отработала 1", sleep(5)])
func2 = lambda: print(["отработала 1", sleep(5)])
func3 = lambda: print(["отработала 1", sleep(5)])

# func1()
# func2()
# func3()

thread1 = threading.Thread(target=func3)
thread2 = threading.Thread(target=func1)
thread3 = threading.Thread(target=func2)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
