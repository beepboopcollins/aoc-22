with open("in.txt", "r") as f:
    raw_in = f.read()

games_raw: list[tuple[str, str]] = [tuple(line.split(" ", 2)) for line in raw_in.split("\n")]


# PART ONE


class GamePartOne:
    _their_moves = ["A", "B", "C"]
    _your_moves = ["X", "Y", "Z"]
    _move_index_name_map: dict[int, str] = {
        0: "Rock",
        1: "Paper",
        2: "Scissors"
    }

    _game_points_map: dict[tuple[int, int], int] = {
        (0, 0): 4,
        (0, 1): 8,
        (0, 2): 3,
        (1, 0): 1,
        (1, 1): 5,
        (1, 2): 9,
        (2, 0): 7,
        (2, 1): 2,
        (2, 2): 6
    }

    def __init__(self, their_move: str, your_move: str):
        self.their_move = self._their_moves.index(their_move)
        self.your_move = self._your_moves.index(your_move)

    @property
    def your_move_name(self):
        return self._move_index_name_map[self.your_move]

    @property
    def their_move_name(self):
        return self._move_index_name_map[self.their_move]

    @property
    def points(self):
        return self._game_points_map[self.their_move, self.your_move]


part_one_games = [GamePartOne(their_move, your_move) for their_move, your_move in games_raw]

out = sum(game.points for game in part_one_games)

with open("OOpt1.txt", "w") as f:
    f.write(str(out))


class GamePartTwo:
    _their_moves = ["A", "B", "C"]
    _outcomes = ["X", "Y", "Z"]
    _move_index_name_map: dict[int, str] = {
        0: "Rock",
        1: "Paper",
        2: "Scissors"
    }
    _outcome_index_name_map: dict[int, str] = {
        0: "Lose",
        1: "Draw",
        2: "Win"
    }
    _game_points_map = {
        (0, 0): 3,
        (0, 1): 4,
        (0, 2): 8,
        (1, 0): 1,
        (1, 1): 5,
        (1, 2): 9,
        (2, 0): 2,
        (2, 1): 6,
        (2, 2): 7
    }

    def __init__(self, their_move: str, outcome: str):
        self.their_move = self._their_moves.index(their_move)
        self.outcome = self._outcomes.index(outcome)

    @property
    def their_move_name(self):
        return self._move_index_name_map[self.their_move]

    @property
    def outcome_name(self):
        return self._outcome_index_name_map[self.outcome]

    @property
    def points(self):
        return self._game_points_map[self.their_move, self.outcome]


part_two_games = [GamePartTwo(their_move, outcome) for their_move, outcome in games_raw]

out = sum(game.points for game in part_two_games)

with open("OOpt2.txt", "w") as f:
    f.write(str(out))
