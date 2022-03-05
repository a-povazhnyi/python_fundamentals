from datetime import datetime


def timeit2(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f'Start Time: {start_time.strftime("%H:%M:%S.%f")}')

        f = func(*args, **kwargs)

        end_time = datetime.now()
        print(f'End Time: {end_time.strftime("%H:%M:%S.%f")}')

        time = end_time - start_time
        print(f'|{func.__name__}| Time Duration: {time}')
        return f
    return wrapper
