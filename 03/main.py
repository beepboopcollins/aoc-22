from dataclasses import dataclass, field


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        raw = f.read()
    return raw


def write_file(filename: str, data: str):
    with open(filename, "w") as f:
        f.write(data)


@dataclass(frozen=True)
class Item:
    _valid_items: str = field(default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", repr=False, init=False)

    letter: str

    def __post_init__(self):
        if len(self.letter) != 1:
            raise ValueError("Item must be a letter")
        if self.letter not in self._valid_items:
            raise ValueError(f"Item must be in {self._valid_items}")

    @property
    def priority(self) -> int:
        return 1 + self._valid_items.index(self.letter)


class Rucksack:

    def __init__(self, inventory: str):
        if len(inventory) % 2:
            raise ValueError("Inventory is not evenly sized.")

        size_of_compartment = len(inventory) // 2

        self.compartment_1 = [Item(item) for item in inventory[:size_of_compartment]]
        self.compartment_2 = [Item(item) for item in inventory[size_of_compartment:]]
        self.inventory = [*self.compartment_1, *self.compartment_2]

    def get_duplicates(self) -> set[Item]:
        return set(item for item in self.compartment_1 if item in self.compartment_2)

    def __repr__(self):
        return f"inventory={self.inventory}"


@dataclass
class Group:
    rucksacks: list[Rucksack]

    def check_item_in_all_rucksacks(self, item: Item) -> bool:
        for rucksack in self.rucksacks:
            if item not in rucksack.inventory:
                return False
        return True

    @property
    def badge(self) -> Item:
        all_items_in_group = set(item for rucksack in self.rucksacks for item in rucksack.inventory)
        potential_badges = set(item for item in all_items_in_group if self.check_item_in_all_rucksacks(item))
        if len(potential_badges) != 1:
            raise ValueError(f"{len(potential_badges)} potential badges found")
        return potential_badges.pop()


def main():
    rucksacks_raw = read_file("in.txt").split("\n")
    rucksacks = [Rucksack(inventory) for inventory in rucksacks_raw]
    duplicates = [rucksack.get_duplicates() for rucksack in rucksacks]
    sum_priorities = sum(dupe_item.priority for dupe_item_rucksack in duplicates for dupe_item in dupe_item_rucksack)
    write_file("pt1.txt", str(sum_priorities))

    size_of_groups = 3
    if len(rucksacks) % size_of_groups:
        raise ValueError(f"cannot create evenly sized groups of size {size_of_groups}, we have {len(rucksacks)} "
                         "rucksacks")
    groups = []
    for first_rucksack_idx in range(0, len(rucksacks), 3):
        groups.append(Group(rucksacks[first_rucksack_idx:first_rucksack_idx + 3]))
    badges = [group.badge for group in groups]
    sum_badge_priorities = sum(badge.priority for badge in badges)
    write_file("pt2.txt", str(sum_badge_priorities))


if __name__ == "__main__":
    main()
