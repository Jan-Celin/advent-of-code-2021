instructions = []
for i in range(252):
    instructions.append(input().split())

for T in range(99999716637353, 11111111111111, -1):
    values = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    digit = 0
    model = str(T)
    if '0' in model:
        continue
    for instruction in instructions:
        if instruction[0] == 'inp':
            values[instruction[1]] = int(model[digit])
            digit += 1
        elif instruction[0] == 'add':
            if instruction[2] in values:
                values[instruction[1]] = values[instruction[1]] + values[instruction[2]]
            else:
                values[instruction[1]] = values[instruction[1]] + int(instruction[2])
        elif instruction[0] == 'mul':
            if instruction[2] in values:
                values[instruction[1]] = values[instruction[1]] * values[instruction[2]]
            else:
                values[instruction[1]] = values[instruction[1]] * int(instruction[2])
        elif instruction[0] == 'div':
            if instruction[2] in values:
                values[instruction[1]] = int(values[instruction[1]] / values[instruction[2]])
            else:
                values[instruction[1]] = int(values[instruction[1]] / int(instruction[2]))
        elif instruction[0] == 'mod':
            if instruction[2] in values:
                values[instruction[1]] = values[instruction[1]] % values[instruction[2]]
            else:
                values[instruction[1]] = values[instruction[1]] % int(instruction[2])
        elif instruction[0] == 'eql':
            if instruction[2] in values:
                values[instruction[1]] = int(values[instruction[1]] == values[instruction[2]])
            else:
                values[instruction[1]] = int(values[instruction[1]] == int(instruction[2]))
    if values['z'] == 0:
        print(T)
        break
