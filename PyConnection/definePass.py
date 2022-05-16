

def setEncoding(encoding):
    if len(encoding) > 3 or len(encoding) <= 0:
        raise Exception("Invalid encoding, out of range  [0,3]")
    password = []
    index = 0
    for number in encoding:
        password.append(int(number))
        index += 1
    return password
