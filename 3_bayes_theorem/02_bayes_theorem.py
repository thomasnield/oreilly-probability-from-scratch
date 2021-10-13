p_gamer_given_homicidal = .85
p_gamer = .19
p_homicidal = .00005

p_homicidal_given_gamer = p_gamer_given_homicidal * p_homicidal / p_gamer

print("Probability of homicidal given gamer: {}".format(p_homicidal_given_gamer))
