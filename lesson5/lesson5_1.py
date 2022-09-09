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


def something(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper


@something
@already_sorted
@totally_unique
def generate_random(length):
    return [random.randint(0, length * 10) for x in range(length)]


if __name__ == '__main__':
    # a = generate_random(length=200)

    # already_sorted(generate_random)(30)
    # print(a, len(a), len(set(a)))
    print(generate_random)
