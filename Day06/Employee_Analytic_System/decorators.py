

from functools import wraps

def log_operation(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    
    return wrapper