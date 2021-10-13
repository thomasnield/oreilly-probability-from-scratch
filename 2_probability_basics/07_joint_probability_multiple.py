prob_failure = .10

three_fails_prob = 1.0 

for i in range(0,3):
    three_fails_prob = three_fails_prob * prob_failure

print("Probability of 3 consecutive failures: {}".format(three_fails_prob))
