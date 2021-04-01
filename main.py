def close10(x, y):
 
    if abs(10 - x) < abs(10 - y):
        return y
    elif abs(10 - x) > abs(10 - y):
        return x
    elif abs(10 - x) == abs(10 - y):
        return 0

print(close10(11, 9))