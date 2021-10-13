

# Factorials multiply consecutive descending integers down to 1
# EXAMPLE: 5! = 5 * 4 * 3 * 2 * 1
def factorial(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

# Generates the coefficient needed for the binomial distribution
def binomial_coefficient(n: int, k: int):
    return factorial(n) / (factorial(k) * factorial(n - k))


# Binomial distribution calculates the probability of k events out of n trials
# given the p probability of k occurring
def binomial_distribution(n: int, k: int, p: float):
    return binomial_coefficient(n, k) * (p ** k) * (1.0 - p) ** (n - k)

p = .9
n = 10

prob_eight_or_less_successes = 0.0

for k in range(0,9):
    prob_of_k_successes = binomial_distribution(n, k, p)
    print("PROB {} SUCCESSES: {}".format(k, prob_of_k_successes))
    prob_eight_or_less_successes += prob_of_k_successes

print("PROB 8 OR LESS SUCCESSES: {}".format(prob_eight_or_less_successes))
# PROB 8 OR LESS SUCCESSES: 0.2639010708999999