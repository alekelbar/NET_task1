

def setEncoding(encoding):
    if len(encoding) < 2:
        raise Exception("Invalid encoding, out of range  [2,n]")
    password = []
    for number in encoding:
        try:
            convertion = int(number)
        except Exception as error:
            raise Exception("Invalid value for encoding", error)
        password.append(convertion)
    return password
