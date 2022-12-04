from dataclasses import dataclass


@dataclass
class Elf:
    start_zone: int
    end_zone: int


@dataclass
class ElfPair:
    elf1: Elf
    elf2: Elf

    def one_contains_two(self) -> bool:
        return (self.elf1.start_zone <= self.elf2.start_zone) and (self.elf1.end_zone >= self.elf2.end_zone)

    def two_contains_one(self) -> bool:
        return (self.elf2.start_zone <= self.elf1.start_zone) and (self.elf2.end_zone >= self.elf1.end_zone)

    def one_contains_other(self) -> bool:
        return self.one_contains_two() or self.two_contains_one()

    def one_ends_in_two(self) -> bool:
        return self.elf2.start_zone <= self.elf1.end_zone <= self.elf2.end_zone

    def two_ends_in_one(self) -> bool:
        return self.elf1.start_zone <= self.elf2.end_zone <= self.elf1.end_zone

    def has_overlap(self) -> bool:
        return self.one_ends_in_two() or self.two_ends_in_one()


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        raw = f.read()
    return raw


def write_file(filename: str, data: str):
    with open(filename, "w") as f:
        f.write(data)


def transform_raw_in(raw_in: list[str]) -> list[list[tuple[int, int]]]:
    raw_pairs = []
    for line in raw_in:
        this_pair = []
        elves = line.split(",")
        for elf in elves:
            start_str, end_str = elf.split("-", 2)
            this_pair.append((int(start_str), int(end_str)))
        raw_pairs.append(this_pair)
    return raw_pairs


def get_pairs(raw_pairs: list[list[tuple[int, int]]]) -> list[ElfPair]:
    return [ElfPair(Elf(*raw_pair[0]), Elf(*raw_pair[1])) for raw_pair in raw_pairs]


def main():
    raw_in = read_file("in.txt").split("\n")
    raw_pairs = transform_raw_in(raw_in)
    pairs = get_pairs(raw_pairs)
    total_fully_contained = sum(pair.one_contains_other() for pair in pairs)
    write_file("pt1.txt", str(total_fully_contained))
    total_overlap = sum(pair.has_overlap() for pair in pairs)
    write_file("pt2.txt", str(total_overlap))


if __name__ == "__main__":
    main()
