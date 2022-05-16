
def decode(msj, encoding):
    clave = encoding
    index = 0
    j = 0
    caracter = ''
    code = ''
    while index != len(msj):
        caracter = msj[index]
        if(ord(caracter) >= 65 and ord(caracter) <= 90):
            caracter = chr(ord(caracter) - clave[j])
            if(ord(caracter) < 65):
                caracter = chr((ord(caracter) - 64) + 90)
        elif ord(caracter) == 126:
            caracter = chr(32)
        code += caracter
        index += 1
        if j < 2:
            j += 1
        else:
            j = 0
    return code
