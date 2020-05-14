p_prize1 = 1.0 / 3.0    # probability of prize in door 1
p_left2_prize1 = .5     # probability of door 2 left given prize in door 1
p_left2 = .5            # probability of door 2 being left

# probability of prize in door 1 given door 2 is left
p_prize1_left2 = p_left2_prize1 * p_prize1 / p_left2

print(p_prize1_left2)
