## DAY 2
# url: https://adventofcode.com/2022/day/2

scores = {
    ('A', 'X'): 1 + 3,
    ('A', 'Y'): 2 + 6,
    ('A', 'Z'): 3 + 0,
    ('B', 'X'): 1 + 0,
    ('B', 'Y'): 2 + 3,
    ('B', 'Z'): 3 + 6,
    ('C', 'X'): 1 + 6,
    ('C', 'Y'): 2 + 0,
    ('C', 'Z'): 3 + 3,
}

with open("input.txt", "r") as f:
    content = f.readlines()

pairs = [tuple(x.strip().split()) for x in content]    

## PART 1 - Rock, paper, scissors

result = sum([scores[x] for x in pairs])
print(f"Part 1: {result}")

## PART 2 - new strategy

# x -> lose
# Y => draw
# z -> win

shapes = {
    ('A', 'X'): ('A', 'Z'),
    ('A', 'Y'): ('A', 'X'),
    ('A', 'Z'): ('A', 'Y'),
    ('B', 'X'): ('B', 'X'),
    ('B', 'Y'): ('B', 'Y'),
    ('B', 'Z'): ('B', 'Z'),
    ('C', 'X'): ('C', 'Y'),
    ('C', 'Y'): ('C', 'Z'),
    ('C', 'Z'): ('C', 'X'),   
}

result = sum([scores[shapes[x]] for x in pairs])
print(f"Part 2: {result}")