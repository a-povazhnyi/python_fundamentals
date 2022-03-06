def str_to_int(line):
    if not isinstance(line, str) and not line.isnumeric():
        raise TypeError('Argument type should be a numeric string.')
    else:
        result = 0
        for digit in line:
            # ord() returns an integer representing the Unicode
            # code point of the character
            # 48 is a number where digits start
            result = result * 10 + (ord(digit) - 48)
        return result
