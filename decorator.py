import time

current_time = time.time()
print(current_time)


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        # Record the end time after the function has run
        end_time = time.time()
        # Print the time taken to run the function
        print(f"{function.__name__} run speed: {end_time - start_time} seconds")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()