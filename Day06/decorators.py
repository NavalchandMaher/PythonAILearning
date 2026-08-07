
#decorators

from time import time


def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper


@decorator
def say_hello():
    print("Hello!")

say_hello()

import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper

@timer_decorator
def long_running_function():
    time.sleep(2)  # Simulate a long-running process
    print("Function completed.")

long_running_function()