counter = 0
def count_paths(node, visited, count, path):
    global counter
    path.append(node)
    if node == "end":
        counter += 1
        return 1
    else:
        if node[0] in lower:
            visited.append(node)
        for i in links[node]:
            print(i, visited)
            if i not in visited:
                count_paths(i, visited, count, path)
    

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

N = 7 #21
links = dict()
for i in range(N):
    link1, link2 = map(str, input().split("-"))
    if link1 in links:
        links[link1].append(link2)
    else:
        links[link1] = [link2]
    if link2 in links:
        links[link2].append(link1)
    else:
        links[link2] = [link1]



count_paths("start", [], 0, [])
print(counter)
