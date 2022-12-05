from dataclasses import dataclass


@dataclass
class Crate:
    letter: str



@dataclass
class CargoMove:
    start: int
    end: int
    quantity: int


@dataclass
class Cargo:
    stacks: list[list[Crate]]

    def apply_move(self, move: CargoMove):
        moving_items = [self.stacks[move.start - 1].pop() for _ in range(move.quantity)]
        self.stacks[move.end - 1].extend(moving_items)

    def apply_move_9001(self, move: CargoMove):
        moving_items = [self.stacks[move.start - 1].pop() for _ in range(move.quantity)][::-1]
        self.stacks[move.end - 1].extend(moving_items)


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        raw = f.read()
    return raw


def write_file(filename: str, data: str):
    with open(filename, "w") as f:
        f.write(data)


def transform_raw_in(raw_in: list[str]):
    bottom_of_pile = raw_in.index('')
    number_of_stacks = max(int(x) for x in raw_in[bottom_of_pile - 1].split(" ") if x != '')
    max_height = bottom_of_pile - 1
    stacks = []
    for stack_number in range(number_of_stacks):
        stack = []
        for stack_idx in range(max_height - 1, -1, -1):
            letter = raw_in[stack_idx][4 * stack_number + 1]
            if letter == ' ':
                break
            stack.append(Crate(letter))
        stacks.append(stack)
    cargo = Cargo(stacks)
    moves = []
    for raw_move in raw_in[bottom_of_pile + 1:]:
        quantity = int(raw_move.split('move', 2)[1].split(' ', 3)[1])
        start = int(raw_move.split('from', 2)[1].split(' ', 3)[1])
        end = int(raw_move.split('to', 2)[1].split(' ', 3)[1])
        moves.append(CargoMove(start, end, quantity))
    return cargo, moves


def main():
    raw_in = read_file("in.txt").split("\n")
    cargo, moves = transform_raw_in(raw_in)
    for move in moves:
        cargo.apply_move(move)
    message = "".join(stack[-1].letter for stack in cargo.stacks)
    write_file("pt1.txt", message)
    cargo, moves = transform_raw_in(raw_in)
    for move in moves:
        cargo.apply_move_9001(move)
    pass
    message_9001 = "".join(stack[-1].letter for stack in cargo.stacks)
    write_file("pt2.txt", message_9001)

if __name__ == "__main__":
    main()
