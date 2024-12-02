left_list = []
right_list = []

with open("input", "r") as input:
    for line in input:
        line = line.split("   ")
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

similarity_score = 0

for i in range(len(left_list)):
    similarity_score += left_list[i] * right_list.count(left_list[i])

print(similarity_score)
