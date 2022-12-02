from itertools import product

with open("in.txt", "r") as f:
    raw_in = f.read()

games = [tuple(line.split(" ")) for line in raw_in.split("\n")]

their_moves = ["A", "B", "C"]
your_moves = ["X", "Y", "Z"]

possible_games = list(product(their_moves, your_moves))

game_points_map = {}

for their_move, your_move in possible_games:
    your_move_index = your_moves.index(your_move)
    their_move_index = their_moves.index(their_move)
    move_points = your_move_index + 1

    if your_move_index == their_move_index:
        outcome_points = 3
    elif your_move_index == (their_move_index + 1) % 3:
        outcome_points = 6
    else:
        outcome_points = 0

    game_points_map[(their_move, your_move)] = outcome_points + move_points

out = sum(game_points_map[game] for game in games)

with open("pt1.txt", "w") as f:
    f.write(str(out))

game_points_map = {}

for their_move, outcome in possible_games:
    their_move_index = their_moves.index(their_move)
    if outcome == "Y":
        outcome_points = 3
        move_points = their_move_index + 1
    if outcome == "X":
        outcome_points = 0
        move_points = (their_move_index + 2)%3 + 1
    if outcome == "Z":
        outcome_points = 6
        move_points = (their_move_index + 1)%3 + 1
    game_points_map[(their_move, outcome)] = outcome_points + move_points

out = sum(game_points_map[game] for game in games)

with open("pt2.txt", "w") as f:
    f.write(str(out))