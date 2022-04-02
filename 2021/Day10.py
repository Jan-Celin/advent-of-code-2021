from collections import deque

illegal = {')': 3, ']': 57, '}': 1197, '>': 25137}
score_points = {')': 1, ']': 2, '}': 3, '>': 4}
open_brackets = ['(', '[', '{', '<']
closed_brackets = [')', ']', '}', '>']



lines = []
for i in range(94):
    true = 1
    line = input()
    expecteds = deque()
    for j, bracket in enumerate(line):
        if bracket in open_brackets:
            expecteds.append(closed_brackets[open_brackets.index(bracket)])
        else:
            expected = expecteds.pop()
            if expected != bracket:
                true = 0
                #score += illegal[bracket]
                break
    if true:
        lines.append(line)

scores = []
for i, line in enumerate(lines):
    score = 0
    expecteds = deque()
    for j, bracket in enumerate(line):
        if bracket in open_brackets:
            expecteds.append(closed_brackets[open_brackets.index(bracket)])
        else:
            expected = expecteds.pop()

    expecteds.reverse()
    for j, bracket in enumerate(expecteds):
        score = score * 5 + score_points[bracket]

    scores.append(score)

scores.sort()
print(scores[len(scores)//2])
        



























