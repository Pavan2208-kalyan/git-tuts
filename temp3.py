def decorator_func(func):
    def wrapper_func():
        print("something has happened before the func")
        func()
        print("something has happened after the func")
    return wrapper_func
@decorator_func

def say_hello():
    print("Hello !!")

say_hello()
