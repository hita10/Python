import time
from typing import Callable

# Decorators
def execution_timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper

@execution_timer
def process_data(data_list: list) -> list:
    time.sleep(0.5)
    return [x * 2 for x in data_list]

processed = process_data([10, 20, 30, 40])

# Context Manager
with open("sample_log.txt", "w") as file:
    file.write("Log entry: Script executed successfully.\n")

print("File successfully created and automatically closed.")