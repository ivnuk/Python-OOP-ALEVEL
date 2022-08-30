import datetime


class Employee:
    def __init__(self, name, salary, tech_stack):
        pass

    def check_salary(self):
        # now = datetime.date(2022, 8, 19)
        now = datetime.date.today()


employee = Employee('Petro', 15, ['python', 'java', 'pascal'])


class DummyClass:
    def __init__(self, length, width, name):
        self.length = length
        self.width = width
        self.name = name
        print(self, f'created at {datetime.datetime.now()}')

    # @classmethod
    # def __new__(cls, *args, **kwargs):
    #     obj = super().__new__(*args, **kwargs)
    #     print(obj, f'created at {datetime.datetime.now()}')
    #     return obj

    # def __del__(self):
    #     print(self, f'destroyed at {datetime.datetime.now()}')
    # del self
    #
    def __str__(self) -> str:
        return f"Dummy object named {self.name} with w: {self.width}"

    def __call__(self):
        return self.width * self.length

    def area(self):
        return self.width * self.length

    def __lt__(self, other):
        return self.area() < other.area()  # self() != DumyClass()

    def __le__(self, other):
        return self() <= other()

    def __gt__(self, other):
        return self() > other()

    def __ge__(self, other):
        return self() >= other()

    def __eq__(self, other):
        return self() == other()

    def __ne__(self, other):
        return self() != other()

    def __bool__(self):
        return len(self.name) > 9

    def __len__(self):
        return self.length

    #
    # def __add__(self, other):
    #     return DummyClass(length=self.length + other.length, width=self.width + other.width,
    #                       name=f"{self.name} {other.name}")

    def __add__(self, other):
        self.length += other.length
        self.width += other.width
        return self


if __name__ == '__main__':
    dummy_obj = DummyClass(length=11, width=13, name='some name')
    dummy_obj2 = DummyClass(length=14, width=13, name='some other name')
    # print(dummy_obj != dummy_obj2)
    # print(dummy_obj())
    # print(bool(dummy_obj2))
    # print(len(dummy_obj))
    print(dummy_obj + dummy_obj2)
    print(dummy_obj.__class__.__name__)

# with open('lesson2_super.py') as fp:
#     fp.read()
# do something


# fp = open('lesson2_super.py')
# do someting
# fp.close()

# middleware:
# user -> request -> proxy -> web app -> route -> |change req| -> view ->  |change response|-> response -> user
