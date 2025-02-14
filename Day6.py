start_ages = input().split(',')

ages = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for i in start_ages:
    ages[int(i)] += 1

for T in range(256):
    new_ages = {0: ages[1], 1: ages[2], 2: ages[3], 3: ages[4], 4: ages[5], 5: ages[6], 6: ages[0] + ages[7], 7: ages[8], 8: ages[0]}
    ages = new_ages
print(sum(ages.values()))
