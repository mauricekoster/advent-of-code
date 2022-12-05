from pathlib import Path
from pprint import pprint
from copy import deepcopy

import re

base_path = Path(__file__).parent
with open(base_path / "input.txt", "r") as f:
    content = f.readlines()

print(content)

stack_lines = []
stack = [None]

while True:
    line = content.pop(0).strip('\n')
    if not line:
        break
    stack_lines.append(line)


last_index = list(map(int, stack_lines.pop().split()))[-1]
for i in range(last_index):
    stack.append([])



pprint(stack_lines)
while stack_lines:
    line = stack_lines.pop()
    for i in range(last_index):
        c = line[1+i*4]
        if c != ' ':
            stack[i+1].append(c)

pprint(stack)
stack_copy = deepcopy(stack)

def move_crates_9000(aantal, van, naar):
    s = []
    # print(f"move {aantal} from {van} to {naar}")
    for _ in range(aantal):
        s.append(stack[van].pop())
    stack[naar].extend(s)

for line in content:
    line = line.strip()
    m = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    if m:
        move_crates_9000(int(m.group(1)), int(m.group(2)), int(m.group(3)))

pprint(stack)
s = ''
for x in stack[1:]:
    s += x[-1]
print(s)    

# Part Two
stack = stack_copy
def move_crates_9001(aantal, van, naar):
    s = []
    print(f"move {aantal} from {van} to {naar}")
    for _ in range(aantal):
        s.append(stack[van].pop())
    s.reverse()
    stack[naar].extend(s)


for line in content:
    line = line.strip()
    m = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    if m:
        move_crates_9001(int(m.group(1)), int(m.group(2)), int(m.group(3)))


pprint(stack)
s = ''
for x in stack[1:]:
    s += x[-1]
print(s)    