from time import sleep


class DummyException(Exception):
    pass


class Employee:
    def __init__(self, email):
        self.email = email
        self.validate()
        # self.name = name
        self.save_email()

    def save_email(self):
        with open('emails.txt', 'a+') as fp:
            fp.write(self.email.lower() + '\n')

    def validate(self):
        with open('emails.txt') as fp:
            if self.email.lower() in fp.read():
                raise DummyException('Email is already taken!')


if __name__ == '__main__':
    a = [1, 2, 3]
    emp = Employee()
    b = dict(
        a=1,
        b=2
    )
    # emp.check_salary() -> Attribute Error
    # print(a[4]) -> index error
    # a() -> type error
    # b['c'] -> Key Error
    print(b.get('b', 4))  # No Error -> return None v
    print(b.get('c', 4))  # No Error -> return 4
    print(getattr(b, 'c', 123))
    # print(blah) -> Name Error

    # line 21
    if b.get('c') is None:
        temp_v = 4
    else:
        temp_v = b['c']

    print("done".upper())

    comprehended_list = [x
                         for x in
                         range(100)
                         ]

    try:
        while 1:
            print("AAAA")
            sleep(1)
    except KeyboardInterrupt:
        print('ooooopsie')
