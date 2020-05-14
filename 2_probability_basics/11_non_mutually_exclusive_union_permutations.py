# Declare possible outcomes for coin and die
first_roll_outcomes = [1, 2, 3, 4, 5, 6]
second_roll_outcomes = [1, 2, 3, 4, 5, 6]

# Combine each outcome between both dice
all_combinations = [(c,d) for c in second_roll_outcomes for d in first_roll_outcomes]

# Find outcomes where first die is 1-4:
first_is_1_thru_4 = [t for t in all_combinations if t[0] in range(1,5)]

# Find outcomes where second die is 1-4:
second_is_1_thru_4 = [t for t in all_combinations if t[1] in range(1,5)]

# Overlap between both die outcomes: 
overlap = set(first_is_1_thru_4).intersection(set(second_is_1_thru_4))
print("OVERLAP: {}".format(overlap))

# Calculate correct probability
correct_probability_either_1_thru_4 = \
    float(len(first_is_1_thru_4) + len(second_is_1_thru_4) - len(overlap)) / len(all_combinations)
    
print("CORRECT PROBABILITY OF EITHER DIE BEING 1-4: {}".format(correct_probability_either_1_thru_4))
