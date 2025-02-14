positions_input = input().split(',')
positions = [int(i) for i in positions_input]

minfuel = 99999999999
for i in range(min(positions), max(positions) + 1):
    fuel = 0
    for j in positions:
        dist = abs(j-i)
        fuel += dist*(dist + 1) / 2
    if fuel < minfuel:
        minfuel = fuel

print(minfuel)
