def multiply(a, b):
    return a * b

def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b >= 0 else -result

