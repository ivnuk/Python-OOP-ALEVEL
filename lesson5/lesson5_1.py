import datetime
import functools
import random


def totally_unique(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        length = args[0] if args else kwargs['length']

        # if args:
        #     length = args[0]
        # else:
        #     length = kwargs['length']
        counter_of_calls = 0
        result = []
        while not (result and len(result) == length):
            result = list(set(func(*args, **kwargs)))
            counter_of_calls += 1
        print('Called:', counter_of_calls, 'times')
        return result

    return wrapper


def already_sorted(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return sorted(func(*args, **kwargs))

    return wrapper  # this will be called


def something(func):  # something ( generate random  )
    @functools.wraps(func)  # save the generate random name
    def wrapper(*args, **kwargs):  # define function to replace generate random
        # Do something before
        value = func(*args, **kwargs)  # generate_random (  )
        # Do something after
        return value  # return the result of generate random ( )

    return wrapper  # return func to replace generate random


def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"Execution took {(end - start).seconds} seconds")
        return result

    return wrapper


@something  # something -> already_sorted(totally_unique)(generate_random)(30)
@execution_time
@already_sorted
@totally_unique
def generate_random(length):
    return [random.randint(0, length * 10) for x in range(length)]


ELEMENTS_DATA = [
    {
        "name": "ele1",
        "t_boil": 0,
        "t_evap": 100
    },
    {
        "name": "ele2",
        "t_boil": -89,
        "t_evap": 14
    },
    {
        "name": "ele3",
        "t_boil": 1500,
        "t_evap": 4200
    }
]


class Element:
    def __init__(self, name, t_boil, t_evap):
        self.name = name
        self.t_boil = t_boil
        self.t_evap = t_evap

    def __str__(self):
        return f"{self.name} {self.t_boil}/{self.t_evap}"

    @staticmethod
    def convert_to(t, scale="C"):
        if scale == 'K':
            t += 273
        elif scale == 'F':
            t = (t - 32) * 5 / 9
        return t

    @classmethod
    def from_dict(cls, data):
        result = []
        for entry in data:
            result.append(cls(**entry))  # cls(**entry) === Element(**entry)
        return result


if __name__ == '__main__':
    # a = generate_random(length=200)
    # el = Element()
    # print(Element.convert_to('F'))
    # print(el.convert_to(154, "F"))
    # already_sorted(generate_random)(30)
    # print(a, len(a), len(set(a)))
    # print(generate_random)
    print(Element.from_dict(ELEMENTS_DATA))
