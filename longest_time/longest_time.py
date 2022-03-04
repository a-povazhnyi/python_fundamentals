def longest_time(hour: int, minute: int, second: int) -> int:
    sample = {hour*3600: hour, minute*60: minute, second: second}
    return sample[max(sample.keys())]
