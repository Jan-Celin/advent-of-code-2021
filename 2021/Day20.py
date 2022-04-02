'''
instructions = input()
empty_row = input()

image = [['.' for i in range(118)] for j in range(9)]
for i in range(100):
    image_row = input()
    image_row_list = []
    for j in image_row:
        image_row_list.append(j)
    image.append(['.' for x in range(9)] + image_row_list + ['.' for x in range(9)])

for i in range(9):
    image.append(['.' for j in range(118)])


for T in range(2):
    new_image = [['.' for j in range(118)] for i in range(118)]
    for i, row in enumerate(image[1:117], start=1):
        for j, element in enumerate(row[1:117], start=1):
            surrounding = [image[i-1][j-1], image[i-1][j], image[i-1][j+1],
                           image[i][j-1], image[i][j], image[i][j+1],
                           image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
            binary = ''
            for k in surrounding:
                if k == '.':
                    binary += '0'
                else:
                    binary += '1'

            location = int(binary, 2)

            new_image[i][j] = instructions[location]

    image = new_image

count = 0
for i, row in enumerate(image):
    for j, element in enumerate(row):
        if element == '#':
            count += 1

print(count)
'''
'''
instructions = input()
empty_row = input()

image = [['.' for i in range(23)] for j in range(9)]
for i in range(5):
    image_row = input()
    image_row_list = []
    for j in image_row:
        image_row_list.append(j)
    image.append(['.' for x in range(9)] + image_row_list + ['.' for x in range(9)])

for i in range(9):
    image.append(['.' for j in range(23)])


for T in range(2):
    new_image = [['.' for j in range(23)] for i in range(23)]
    for i, row in enumerate(image[1:22], start=1):
        print(i)
        for j, element in enumerate(row[1:22], start=1):
            surrounding = [image[i-1][j-1], image[i-1][j], image[i-1][j+1],
                           image[i][j-1], image[i][j], image[i][j+1],
                           image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
            binary = ''
            for k in surrounding:
                if k == '.':
                    binary += '0'
                else:
                    binary += '1'
            
            location = int(binary, 2)
            if i == 11 and j == 9:
                print("\n")
                for x, r in enumerate(image):
                    s = ''
                    for y, e in enumerate(r):
                        if x == i and y == j:
                            s += 'X'
                        else:
                            s += e
                    print(s)
                print(surrounding)
                print(binary)
                print(location)
                print("\n")
            new_image[i][j] = instructions[location]

    image = new_image

    count = 0
    for i, row in enumerate(image):
        s = ''
        for j, element in enumerate(row):
            s += element
            if element == '#':
                count += 1
        print(s[:18])
print(count)
'''

instructions = input()
empty_row = input()

image = [['.' for i in range(400)] for j in range(150)]
for i in range(100):
    image_row = input()
    image_row_list = []
    for j in image_row:
        image_row_list.append(j)
    image.append(['.' for x in range(150)] + image_row_list + ['.' for x in range(150)])

for i in range(150):
    image.append(['.' for j in range(400)])

#118 --> 100 + (2*9) --> 100 + (2*50) --> 200
for T in range(50):
    new_image = [['.' for j in range(400)] for i in range(400)]
    for i, row in enumerate(image[1:399], start=1):
        for j, element in enumerate(row[1:399], start=1):
            surrounding = [image[i-1][j-1], image[i-1][j], image[i-1][j+1],
                           image[i][j-1], image[i][j], image[i][j+1],
                           image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
            binary = ''
            for k in surrounding:
                if k == '.':
                    binary += '0'
                else:
                    binary += '1'
            
            location = int(binary, 2)
            new_image[i][j] = instructions[location]
    image = new_image
    for x, r in enumerate(new_image):
        for y, e in enumerate(r):
            if x == 0 or y == 0 or x == 399 or y == 399:
                if T % 2 == 0:
                    image[x][y] = '#'
                else:
                    image[x][y] = '.'
    count = 0
    for i, row in enumerate(image):
        for j, element in enumerate(row):
            if element == '#':
                count += 1
print(count)




