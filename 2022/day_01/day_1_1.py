from pprint import pprint

with open("input.txt", "r") as f:
    content = f.read()

pprint(max([sum(cal) for cal in [map(int, elf.split('\n')) for elf in content.split('\n\n')]]))