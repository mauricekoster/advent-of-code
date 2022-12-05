from pathlib import Path

base_path = Path(__file__).parent
with open(base_path / "input.txt", "r") as f:
    content = f.readlines()

# Part One
def included(a, b):
    return a[0] <= b[0] and a[1] >= b[1]

solution = []
for line in content:
    elf_a, elf_b = line.strip().split(',')
    elf_a = tuple(map(int, elf_a.split('-')))
    elf_b = tuple(map(int, elf_b.split('-')))

    if included(elf_a, elf_b) or included(elf_b, elf_a):
        # print(f"{elf_a} {elf_b}")
        solution.append((elf_a, elf_b))

print(f"Part 1: {len(solution)}")

# Part Two
def overlapping(a, b):
    if a[0] <= b[0] and a[1] <= b[1] and a[1] >= b[0]:
        return True

    if a[0] >= b[0] and a[1] >= b[1] and a[0] <= b[1]:
        return True

    if a[0] >= b[0] and a[1] <= b[1]:
        return True

    if a[0] <= b[0] and a[1] >= b[1]:
        return True

    return False

solution = []
for line in content:
    elf_a, elf_b = line.strip().split(',')
    elf_a = tuple(map(int, elf_a.split('-')))
    elf_b = tuple(map(int, elf_b.split('-')))

    if overlapping(elf_a, elf_b):
        # print(f"{elf_a} {elf_b}")
        solution.append((elf_a, elf_b))

print(f"Part 2: {len(solution)}")
