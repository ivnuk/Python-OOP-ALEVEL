import traceback
from datetime import datetime


class EmailIsAlreadyTakenException(Exception):
    pass


class Employee:
    def __init__(self, name, salary, email):
        self.email = email
        self.validate_email()
        self.name = name
        self.salary = salary
        self.save_email()

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


def main():
    emp = Employee("John", 123, 'johndoe1222@gmail.com')
    emp2 = Employee("Jane", 123, 'janedoe111@gmail.com')
    emp3 = Employee("John", 14, "johnDoe@gmail.com")


if __name__ == '__main__':
    try:
        main()
    except EmailIsAlreadyTakenException:
        with open('logs.txt', 'a+') as fp:
            fp.write(f"{datetime.now()} | {traceback.format_exc()}")
    # with open('emails.txt', 'a+') as fp:
    #     print(fp.read())
    #     fp.seek(0)
    #     print(fp.read())
    #     fp.seek(1)
    #     print(fp.read())
    #     a = fp.readlines()
