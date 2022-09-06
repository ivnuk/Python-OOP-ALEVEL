import traceback
from datetime import datetime

from lesson4.lesson4 import DummyException


def divider(a, b):
    return a / b


def main():
    while 1:
        try:
            a = int(input("Enter a:"), 10)
            b = int(input("Enter b:"), 10)
            result = divider(a, b)
        except ValueError:
            print("Enter real number")
        except ZeroDivisionError as err:
            print("Can't divide by zero")
        else:
            print(result)
        finally:
            print('___________________________')


if __name__ == '__main__':
    try:
        main()
    except DummyException:
        log_message = f"{datetime.now()} \n {traceback.format_exc()}"
