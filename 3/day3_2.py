import re

with open("input", "r") as input:
    file = input.read()

split_contents = []
for i, substring in enumerate(file.split("don't()")):
    if i == 0:
        if substring[0:6] != "don't()":
            split_contents.append(substring)
            continue
    index = substring.find("do()")
    if index != -1:
        split_contents.append(substring[index:])

mul_regex = re.compile("(mul\\([0-9]*,[0-9]*\\))")

valid_instructions = []
for substring in split_contents:
    valid_instructions = valid_instructions + mul_regex.findall(substring)

mul_sum = 0

for instruction in valid_instructions:
    str_operands = instruction.strip("mul(").strip(")").split(",")
    int_operands = [int(operand) for operand in str_operands]
    mul_sum += (int_operands[0] * int_operands[1])

print(mul_sum)
