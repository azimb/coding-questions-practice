def addBinary(a, b):
    a_bin = bin(a)
    b_bin = bin(b)

    a_dec = int(a_bin)
    b_dec = int(b_bin)

    print("a_dec: " + str(a_dec))
    print("b_dec: " + str(b_dec))

    result_int = a_dec + b_dec

    print("result_int: " + str(result_int))

    result_bin = bin(result_int)

    print("result_bin: " + str(result_bin))

    result_str = str(result_bin)

    print("result_str: " + result_str)

    return result_str[2:]

print(addBinary("11", "1"))