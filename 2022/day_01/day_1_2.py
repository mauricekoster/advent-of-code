from pprint import pprint

with open("input.txt", "r") as f:
    content = f.read()


elfs = []
for elf in content.split('\n\n'):
    calories = [int(x) for x in elf.split('\n')]
    elfs.append(sum(calories))

elfs.sort()
pprint(sum(elfs[-3:]))