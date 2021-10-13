import math, random

# normal distribution, returns likelihood
def normal_pdf(x: float, mean: float, std_dev: float) -> float:
    return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * \
        math.exp(-1.0 * ((x - mean) ** 2 / (2.0 * std_dev ** 2)))

def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)

    return total_sum * delta_x

def dog_weight_distribution(x):
    mean = 64.43
    std_dev = 2.99
    return normal_pdf(x, mean, std_dev)

prob_between_62_and_66 = approximate_integral(a=62, b=66, n=1000, f=dog_weight_distribution)

print("PROB BETWEEN 62 and 66: {}".format(prob_between_62_and_66))
# PROB BETWEEN 62 and 66: 0.4920450456930307