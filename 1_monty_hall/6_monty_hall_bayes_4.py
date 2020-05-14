
p_prize77 = 1.0 / 1000.0        # probability of prize in door 77
p_left77_prize77 = 1.0          # probability of door 77 left given prize in door 77
p_left77 = 1.0 / 999.0          # probability of door 77 being left

# probability of prize in door 1 given door 2 is left
p_prize77_left77 = p_left77_prize77 * p_prize77 / p_left77

print(p_prize77_left77)
