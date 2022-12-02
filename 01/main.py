with open("in.txt", "r") as f:
    raw_in = f.read()

out = max([sum([int(calorie) for calorie in elf_inv]) for elf_inv in [elf.split("\n") for elf in raw_in.split("\n\n")]])

with open("pt1.txt", "w") as f:
    f.write(str(out))

out = sum(sorted([sum([int(calorie) for calorie in elf_inv]) for elf_inv in [elf.split("\n") for elf in raw_in.split("\n\n")]])[-3:])

with open("pt2.txt", "w") as f:
    f.write(str(out))