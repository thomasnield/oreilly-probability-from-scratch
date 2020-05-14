p_prize19 = 1.0 / 1000.0          # probability of prize in door 19
p_left77_prize19 = 1.0 / 999.0    # probability of door 77 left given prize in door 19
p_left77 = 1.0 / 999.0            # probability of door 77 being left

# probability of prize in door 19 given door 77 is left
p_prize19_left77 = p_left77_prize19 * p_prize19 / p_left77

print(p_prize19_left77)
