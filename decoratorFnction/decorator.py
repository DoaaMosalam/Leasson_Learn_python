def check(func):  # is a decorator function as  it takes a functon (need to be enhanced) as its parameter
    def inside(a, b):
        if b == 0:
            print("cannot divide by zero")
            return
        func(a, b)

    return inside


def div(a, b):
    return a / b


div = check(div)

print(div(10, 0))
print("===========================================================")
def decorator(func):
    def wrapper():
        print("Before original function")
        func()
        print("After original function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


def check(func):  # is a decorator function as  it takes a functon (need to be enhanced) as its parameter
    def inside(a, b):
        if b == 0:
            print("cannot divide by zero")
            return
        return func(a, b)

    return inside


@check
def div(a, b):
    return a / b


# div=check(div)

print(div(10, 2))
