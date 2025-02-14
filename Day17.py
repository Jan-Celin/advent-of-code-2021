def break_condition(curr_loc):
    if curr_loc[0] > x2 or curr_loc[1] < y1:
        return True

x1 = 60
x2 = 94
y1 = -171
y2 = -136
"""
x1 = 20
x2 = 30
y1 = -10
y2 = -5
"""
max_max_height = [0]
count = 0
for i in range(10, 100):
    for j in range(-1000,1000):
        location = [0,0] #[x, y]
        velocity = [i,j] #forward, upward
        correct = 0
        heights = []
        while True:
            heights.append(location[1])
            if break_condition(location):
                heights = []
                break
            
            if (location[0] >= x1 and location[0] <= x2) and (location[1] >= y1 and location[1] <= y2):
                #correct = 1
                #max_height = max(heights)
                count += 1
                break
            location[0] += velocity[0]
            location[1] += velocity[1]
            if velocity[0] != 0:
                velocity[0] -= 1
            velocity[1] -= 1
            
        #if correct:
        #    if max_max_height[0] < max_height:
        #        max_max_height = [max_height, i, j, location]
print(count)
