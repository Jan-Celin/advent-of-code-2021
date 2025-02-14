valid = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'acf']

result = 0
for T in range(200):
    signal, output = map(str, input().split('|'))
    signal = signal.split()
    output = output.split()
    segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    key = {}
    found = 0
    for i1 in segments:
        key[i1] = 'a'
        segments2 = [x for x in segments]
        segments2.remove(i1)
        for i2 in segments2:
            key[i2] = 'b'
            segments3 = [x for x in segments2]
            segments3.remove(i2)
            for i3 in segments3:
                key[i3] = 'c'
                segments4 = [x for x in segments3]
                segments4.remove(i3)
                for i4 in segments4:
                    key[i4] = 'd'
                    segments5 = [x for x in segments4]
                    segments5.remove(i4)
                    for i5 in segments5:
                        key[i5] = 'e'
                        segments6 = [x for x in segments5]
                        segments6.remove(i5)
                        for i6 in segments6:
                            
                            key[i6] = 'f'
                            segments7 = [x for x in segments6]
                            segments7.remove(i6)
                            
                            key[segments7[0]] = 'g'

                            correct = 1
                            for j in signal:
                                new_num = ''
                                for char in j:
                                    new_num += key[char]
                                sorted_chars = sorted(new_num)
                                new_num = "".join(sorted_chars)
                                if new_num not in valid:
                                    correct = 0
                            for j in output:
                                new_num = ''
                                for char in j:
                                    new_num += key[char]
                                sorted_chars = sorted(new_num)
                                new_num = "".join(sorted_chars)
                                if new_num not in valid:
                                    correct = 0
                                
                            if correct == 1:
                                print(T)
                                found = 1
                                number = ''
                                for k in output:
                                    new_num = ''
                                    for char in k:
                                        new_num += key[char]
                                    digit = str(valid.index("new_num"))
                                    number += digit
                                number = int(number)
                                result += number
                        if found:
                            print(1)
                            break
                    if found:
                        print(1)
                        break
                if found:
                    print(1)
                    break
            if found:
                print(1)
                break
        if found:
            print(1)
            break

print(result)
                                    
'''
total = 0
for T in range(200):
    values = {0: '',1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    signal, output = map(str, input().split('|'))
    signal = signal.split()
    output = output.split()
    not_found = 4
    for j in signal:
        j.sort()
        if len(j) == 2:
            values[1] = j
        elif len(j) == 3:
            values[7] = j
        elif len(j) == 4:
            values[4] = j
        elif len(j) == 7:
            values[8] = j
    for j in output:
        j.sort()
        if len(j) == 2:
            not_found -= 1
            values[1] = j
        elif len(j) == 3:
            not_found -= 1
            values[7] = j
        elif len(j) == 4:
            not_found -= 1
            values[4] = j
        elif len(j) == 7:
            not_found -= 1
            values[8] = j
    while not_found:
        for i in signal:
            if i in values:
                continue
        
print(count)
'''
