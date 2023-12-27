import threading


def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
    return wrapper


@printer
def reverse_num(number):
    return int(str(number)[::-1])


num1 = input("num_1: ")
num2 = input("num_2: ")


thread1 = threading.Thread(target=reverse_num, args=(num1,))
thread2 = threading.Thread(target=reverse_num, args=(num2,))


thread1.start()
thread2.start()

thread1.join()
thread2.join()
