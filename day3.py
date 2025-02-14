n = 1000
nums = [[],[],[],[],[],[],[],[],[],[],[],[]]
numbersmain = []
for i in range(n):
    num = input()
    nums[0].append(num[0])
    nums[1].append(num[1])
    nums[2].append(num[2])
    nums[3].append(num[3])
    nums[4].append(num[4])
    nums[5].append(num[5])
    nums[6].append(num[6])
    nums[7].append(num[7])
    nums[8].append(num[8])
    nums[9].append(num[9])
    nums[10].append(num[10])
    nums[11].append(num[11])

    numbersmain.append(num)
    
##ox = ''
##co = ''
##for i in range(12):
##    if nums[i].count('1') >= nums[i].count('0'):
##        print(1)
##        for j in numbers:
##            if j[i] != '1':
##                numbers.remove(j)
##    else:
##        print(0)
##        for j in numbers:
##            if j[i] != '0':
##                numbers.remove(j)
##    print(numbers)
##    if len(numbers) == 1:
##        ox = numbers[0]
##
##for i in range(12):
##    if nums[i].count('1') >= nums[i].count('0'):
##        for j in numbers:
##            if j[i] != '0':
##                numbers.remove(j)
##    else:
##        for j in numbers:
##            if j[i] != '1':
##                numbers.remove(j)
##    if len(numbers) == 1:
##        co = numbers[0]
##
##print(int(ox,2) * int(co,2))

numbers = numbersmain
#while True:
    

for k in range(12):
    if len(numbers) == 1:
        break
    num0 = 0
    num1 = 0
    for i in numbers:
        if i[k] == '0':
            num0 += 1
        else:
            num1 += 1
    if num0 > num1:
        numbers = [x for x in numbers if x[k] == '0']
    else:
        numbers = [x for x in numbers if x[k] == '1']
    
print(numbers[0])

numbers = numbersmain
#while True:
    

for k in range(12):

    if len(numbers) == 1:
        break

    num0 = 0
    num1 = 0

    for i in numbers:
        if i[k] == '0':
            num0 += 1
        else:
            num1 += 1
    if num0 > num1:
        numbers = [x for x in numbers if x[k] == '1']
    else:
        numbers = [x for x in numbers if x[k] == '0']


print(numbers[0])

















        





        
