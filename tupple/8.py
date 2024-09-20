def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

s = add(3, 4)
print(s)
print(add(3, 4))
