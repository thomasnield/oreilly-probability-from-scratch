def odds_to_prob(odds):
	return odds / (1.0 + odds)
	
defective_odds = 1.5
defective_probability = odds_to_prob(defective_odds)
print(defective_probability)
