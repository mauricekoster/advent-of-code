from pathlib import Path

base_path = Path(__file__).parent
with open(base_path / "input.txt", "r") as f:
    content = f.readlines()


prio = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

## Part 1
print("-- PART ONE --")
priorities = []
for line in content:
    line = line.strip()
    half = int(len(line) / 2)
    a, b = line[:half], line[half:]
    
    l = list(set(a) & set(b))
    l = sum([prio.index(x) for x in l])
    priorities.append(l)
    print(f"{a} {b} -> {l}")

print(f"Sum of priorities; {sum(priorities)}")

# Part 2
print("-- PART TWO --")
priorities = []
while content:
    elf1 = content.pop(0).strip()
    elf2 = content.pop(0).strip()
    elf3 = content.pop(0).strip()
    l = list(set(elf1) & set(elf2) & set(elf3))
    l = sum([prio.index(x) for x in l])
    print(f" -> {l}")
    priorities.append(l)
print(f"Sum of priorities; {sum(priorities)}")