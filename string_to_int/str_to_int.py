def str_to_int(line):
    if isinstance(line, str) and line.isnumeric():
        result = 0
        for digit in line:
            result = result * 10 + (ord(digit) - 48)
        return result
    raise TypeError('Argument type should be a numeric string.')
