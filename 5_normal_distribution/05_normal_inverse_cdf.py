import random
from scipy.special import erfinv

# the quantile function, also known as inverse CDF 
def inv_normal_cdf(p: float, mean: float, std_dev: float):
    return mean + (std_dev * (2.0 ** 0.5) * erfinv((2.0 * p) - 1.0))

mean = 64.43
std_dev = 2.99

# generate 10 random values following 
# normal distribution 
for i in range(0,10):
    random_p = random.uniform(0.0, 1.0)
    print(inv_normal_cdf(random_p, mean, std_dev))
