from datetime import datetime
import logging


log = logging.getLogger()
log.setLevel(logging.INFO)

console = logging.StreamHandler()
log.addHandler(console)


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.utcnow()
        log.info(f'Start Time: {start_time.strftime("%H:%M:%S.%f")}')

        f = func(*args, **kwargs)

        end_time = datetime.utcnow()
        log.info(f'Start Time: {end_time.strftime("%H:%M:%S.%f")}')

        time = end_time - start_time
        log.info(f'|{func.__name__}| Time Duration: {time}')
        return f
    return wrapper
