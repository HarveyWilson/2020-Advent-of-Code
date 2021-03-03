with open('Day 8\\input.txt') as f:
    data = f.readlines()

instructions = [d.strip() for d in data]

changed_instructions = []

for i,instruct in enumerate(instructions):
    tmp_instruc = instructions.copy()
    if tmp_instruc[i][:3] == "nop":
        tmp_instruc[i] = "jmp" + instructions[i][3:]
        changed_instructions.append(tmp_instruc)
        continue
    if tmp_instruc[i][:3] == "jmp":
        tmp_instruc[i] = "nop" + instructions[i][3:]
        changed_instructions.append(tmp_instruc)

for instruct in changed_instructions:
    acc = 0
    step = 0
    steps = []
    while step not in steps:
        if step >= 638:
            print(step, acc)
            break
        steps.append(step)
        cmd = instruct[step][:3]
        val = int(instruct[step][3:])
        if cmd == "nop":
            step += 1
        if cmd == "acc":
            acc += val
            step += 1
        if cmd == "jmp":
            step += val
