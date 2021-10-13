population = 100000.0

p_gamer_given_homicidal = .85
p_gamer = .19
p_homicidal = .00005

gamers_ct = population * p_gamer
homicidal_criminals_ct = population * p_homicidal
gamers_and_homicidal_ct = homicidal_criminals_ct * p_gamer_given_homicidal

print("#Gamers: {}".format(gamers_ct))
print("#Homicidal Criminals: {}".format(homicidal_criminals_ct))
print("#Gamers who are homicidal criminals: {}".format(gamers_and_homicidal_ct))
