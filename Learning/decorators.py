# function as decorators
def escape_encode(f):
    # a decorator function to convert any value to ascii value.
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


# class as decorator
class CallCount:
    # a class decorator to count number of calls for decorated function.
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


# usage of class as decorator
@CallCount
def say_hello(name):
    print('Hello {}!'.format(name))


# class instance as decorators
class Trace:
    # a class whose instance used as decorator.
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


# usage of class instance as decorator
tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


# Decorating class Methods
class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix


# usage of decorated class method.
im = IslandMaker('island')
im.make_island('Python')


# output : Python island

# Parameterized Decorator
# the decorator will help in validating the argument of a function.
def check_non_negative(index):
    def validator(f):
        def wraps(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must be non negative'.format(args[index]))

        return wraps

    return validator


# usage of parameterized decorator.
@check_non_negative(1)
def create_list(value, size):
    return value * size
