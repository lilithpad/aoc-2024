import re

with open("input", "r") as input:
    file = input.read()

mul_regex = re.compile("(mul\\([0-9]*,[0-9]*\\))")

valid_instructions = mul_regex.findall(file)

mul_sum = 0

for instruction in valid_instructions:
    str_operands = instruction.strip("mul(").strip(")").split(",")
    int_operands = [int(operand) for operand in str_operands]
    mul_sum += (int_operands[0] * int_operands[1])

print(mul_sum)
