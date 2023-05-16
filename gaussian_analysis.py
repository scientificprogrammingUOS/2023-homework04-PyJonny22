import numpy as np

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if not all(isinstance(param, (int, float)) for param in [loc, scale, lower_bound, upper_bound]):
        raise ValueError("loc, scale, lower_bound, and upper_bound must be integers or floats.")

    if lower_bound >= upper_bound:
        raise ValueError("lower_bound must be smaller than upper_bound.")

    samples = np.random.normal(loc=loc, scale=scale, size=100)
    filtered_samples = samples[(samples >= lower_bound) & (samples <= upper_bound)]

    return np.mean(filtered_samples), np.std(filtered_samples)

if __name__ == "__main__":
    loc = 0
    scale = 1
    lower_bound = -1
    upper_bound = 1

    mean, std = gaussian_analysis(loc, scale, lower_bound, upper_bound)
    print("Mean:", mean)
    print("Standard Deviation:", std)
