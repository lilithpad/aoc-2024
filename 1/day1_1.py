left_list = []
right_list = []

with open("input", "r") as input:
    for line in input:
        line = line.split("   ")
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

left_list.sort()
right_list.sort()

difference_sum = 0
for i in range(len(left_list)):
    difference_sum += max(left_list[i], right_list[i]) - min(left_list[i], right_list[i])

print(difference_sum)
