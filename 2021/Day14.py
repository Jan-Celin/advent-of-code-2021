"""
import collections

polymer = input()

empty_line = input()

instructions = {}
count_pairs = {}
for i in range(100):
    instruction = input().split(" -> ")
    instructions[instruction[0]] = instruction[1]
    count_pairs[instruction[0]] = polymer.count(instruction[0])
    

for k in range(1):
    newpolymer = [0 for i in range(len(polymer) * 2)]
    
    j = 0
    for i in range(len(polymer)):
        newpolymer[j] = polymer[i]
        newpolymer[j+1] = []
        j += 2

    for i in range(0, len(newpolymer) - 2, 2):
        newpolymer[i+1] = instructions[newpolymer[i] + newpolymer[i+2]]

    polymer = newpolymer[:-1]


count = collections.Counter(polymer)
most_common = str(max(count, key = count.get))

count = collections.Counter(polymer)
least_common = str(min(count, key = count.get))

most_common1 = [polymer.count(most_common), most_common]
least_common1 = [polymer.count(least_common), least_common]

opolymer = polymer

"""






polymer = input()

empty_line = input()

instructions = {}
count_pairs = {}
for i in range(100):
    instruction = input().split(" -> ")
    instructions[instruction[0]] = instruction[1]
    count_pairs[instruction[0]] = polymer.count(instruction[0])

count_letters = {}
for letter in 'ABCDEFGHIJKLMNOPQRTSUVWXYZ':
    count_letters[letter] = polymer.count(letter)

ncount_pairs = dict()
for j in range(40):
    ncount_pairs = count_pairs.copy()
    for i in count_pairs:
        if count_pairs[i] == 0:
            continue
        
        new_letter = instructions[i]
        ncount_pairs[i] -= count_pairs[i]
        ncount_pairs[i[0] + new_letter] += count_pairs[i]
        ncount_pairs[new_letter + i[1]] += count_pairs[i]
        count_letters[new_letter] += count_pairs[i]
    count_pairs = ncount_pairs.copy()

ncount_letters = count_letters.copy()
for i in count_letters:
    if count_letters[i] == 0:
        del ncount_letters[i]

count_letters = ncount_letters
print(count_letters[max(count_letters, key=count_letters.get)] - count_letters[min(count_letters, key=count_letters.get)])








"""
CH --> N

CN --> 4
NH --> 4
N --> 8
"""





