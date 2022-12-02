with open("in.txt", "r") as f:
    raw_in = f.read()

out = max([sum([int(calorie) for calorie in elf_inv]) for elf_inv in [elf.split("\n") for elf in raw_in.split("\n\n")]])

with open("out.txt", "w") as f:
    f.write(str(out))