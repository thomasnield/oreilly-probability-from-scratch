from random import randint, choice


def random_door():
    return randint(1, 3)


trial_count = 10000

stay_wins = 0
switch_wins = 0

for i in range(0, trial_count):
    prize_door = random_door()
    selected_door = random_door()
    opened_door = choice([d for d in range(1, 4) if d != selected_door and d != prize_door])
    switch_door = choice([d for d in range(1, 4) if d != selected_door and d != opened_door])

    if selected_door == prize_door:
        stay_wins += 1

    if switch_door == prize_door:
        switch_wins += 1

print("STAY WINS: {}, SWITCH WINS: {}".format(stay_wins, switch_wins))

print("STAY WIN RATE: {}, SWITCH WIN RATE: {}".format(float(stay_wins)/float(trial_count), float(switch_wins)/float(trial_count)))
