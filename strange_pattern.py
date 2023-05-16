import numpy as np

def strange_pattern(shape):
    n, m = shape
    pattern = np.zeros((n, m), dtype=bool)
    pattern[:m:3, 0::3] = True
    pattern[1:m:3, 2::3] = True
    pattern[2:m:3, 1::3] = True
    return pattern

if __name__ == "__main__":
    shape = (10, 10)
    result = strange_pattern(shape)
    print(result)