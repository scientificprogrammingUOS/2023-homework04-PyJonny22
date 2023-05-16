import numpy as np

def combination(a, b, axis=0):
    a = np.squeeze(a)
    b = np.squeeze(b)
    
    #if a.ndim != 1 or b.ndim != 1:
        #raise ValueError("Input arrays must be one-dimensional.")
    
    if axis != 0:
        raise ValueError("Only axis 0 is currently supported.")

    #elif a.shape != b.shape:
        #raise ValueError("Input arrays must have the same shape.")

    else: 
        combined_array = np.concatenate((a, b), axis=axis)
    
        return combined_array
    
if __name__ == "__main__":

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    combined = combination(a, b)
    print("Combined Array:", combined)
    
