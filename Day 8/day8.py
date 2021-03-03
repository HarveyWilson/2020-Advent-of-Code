with open('Day 8\\input.txt') as f:
    data = f.readlines()

instructions = [d.strip() for d in data]
acc = 0
step = 0
steps = []

while step not in steps:
    steps.append(step)
    cmd = instructions[step][:3]
    val = int(instructions[step][3:])
    if cmd == "nop":
        step += 1
        continue
    if cmd == "acc":
        acc += val
        step += 1
        continue
    if cmd == "jmp":
        step += val
        continue
print(step, acc)