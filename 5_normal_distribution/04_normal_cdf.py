import math, random

# cumulative density function, returns area/probability up to x 
def normal_cdf(x: float, mean: float, std_dev: float) -> float:
    return (1 + math.erf((x - mean) / math.sqrt(2) / std_dev)) / 2


mean = 64.43
std_dev = 2.99

prob_between_62_and_66 = normal_cdf(66.0, mean, std_dev) - normal_cdf(62.0, mean, std_dev)

print("PROB BETWEEN 62_and_66: {}".format(prob_between_62_and_66))
# PROB BETWEEN 62_and_66: 0.49204501470628936