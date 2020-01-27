# from future import print_function

def myDecorator(func):
    def wrapper(a,b, *args, **kwargs):
        print(f"Calling testFunc: {(a,b,*args)}, {**kwargs}")
        return func()
        print(f"Finished {a+b}")
    return wrapper
