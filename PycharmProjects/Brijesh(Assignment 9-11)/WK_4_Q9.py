def ascii(string):
    ascii={chr(i):i for i in range(256) if chr(i) in string}
    result={i:ascii[i] for i in string}
    print("result : ", result)
    print("List of ascii : ", end="")
    return [i for i in result.values()]
print(ascii("Brijesh"))