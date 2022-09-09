import functools
import traceback
from datetime import datetime


class EmailIsAlreadyTakenException(Exception):
    pass


def traceback_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as err:
            print(err)
            with open('logs.txt', 'a+') as fp:
                fp.write(f"{datetime.now()} | {traceback.format_exc()}")
        else:
            return result

    return wrapper


class Employee:
    def __init__(self, name, last_name, salary, email):
        self.email = email
        self.validate_email()
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.save_email()

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

    @property
    def common_salary(self):
        return self.salary * 20

    def save_email(self):
        with open('emails.txt', 'a+') as fp:
            # fp.seek(0)
            # fp.read()  # nothing / with seek get full file
            fp.write(self.email.lower())

    def validate_email(self):
        with open('emails.txt', 'a+') as fp:
            fp.seek(0)
            if self.email.lower() in fp.read():
                raise EmailIsAlreadyTakenException()


@traceback_logger
def main():
    emp = Employee("John", "Doe", 123, 'johndoe1222@gmail.com')
    emp2 = Employee("Jane", "Doe", 123, 'janedoe111@gmail.com')
    emp3 = Employee("John", "Smith", 14, "johnDoe@gmail.com")

    print(emp.full_name)
    print(emp.common_salary)


if __name__ == '__main__':
    main()
