def reverse_len(array) -> int:
    for element in array[::-1]:
        yield len(element)
