def close10(x, y):
    if 10 - x < 10 - 7:
        return x
    elif 10 - x > 10 - y:
        return y
    elif 10 - x + 10 - y:
        return 0

print(close10(12, 88))