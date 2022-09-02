"""
Lesson 3 pep examples live here.

order -> imports -> constant -> function definitions -> class definitions -> other code
"""
import datetime as dt
import os
import sys

# from django import views


SOME_CONSTANT = "AB\"C"
SOME_OTHER_CONSTANT = 'AB\'CDE'

# some_dict['key']

a, b, c = set(), set(), set()

# d is unions of a and b sets -> collect unique ids from internal and external users to process to the db
d = b.union(a)


class A:
    """class "A" """

    def __init__(self):
        pass

    def _secret_meth(self, a, b):
        return 1 + 2, 3 == 5

    def method1(self, c=None):
        """
        do nothing
        :param c: some parameter
        :return: Nothing
        """
        pass

    def method2(self):
        return [][:]

    def get_date(self, date_list):
        """
        Get the parsed parts of datetime.
        Example: [yyyy, mm, dd]
        :param date_list:
        :return: str
        """
        return "a"

    def get_date_2(self, days: int = None, current_date: dt.date = None):
        days_amount = 0
        if days is not None:
            pass
        elif current_date is not None:
            pass
        else:
            pass
        return days_amount * self.salary


class B:
    pass


def func():
    pass


# some code

# some other code


if __name__ == '__main__':
    # some code here

    for i in range(10):
        print(i)

    # some other code here
    os.environ.get('')

    # if 1:
    #     pass
    # elif 2:
    #     pass
    # elif 3:
    #     pass
    # else:
    #     pass
    a = A()
    # a.get_date()

