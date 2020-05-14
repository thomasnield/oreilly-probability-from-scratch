p_prize2 = 1.0 / 3.0    # probability of prize in door 2
p_left2_prize2 = 1.0    # probability of door 2 left given prize in door 2
p_left2 = .5            # probability of door 2 being left 

# probability of prize in door 2 given door 2 is left
p_prize2_left2 = p_left2_prize2 * p_prize2 / p_left2

print(p_prize2_left2)
