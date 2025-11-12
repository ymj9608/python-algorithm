N = int(input())
expression = input()

num_dict = {}
values = []

for i in range(N):
    values.append(int(input()))

for i in range(N):
    code = ord('A') + i
    char = chr(code)
    num_dict[char] = values[i]

stack = []

for char in expression:
    if char.isalpha():
        num = num_dict[char]
        stack.append(num)
    else:
        num_2 = stack.pop()
        num_1 = stack.pop()

        if char == '+':
            result = num_1 + num_2
        elif char == '-':
            result = num_1 - num_2
        elif char == '*':
            result = num_1 * num_2
        elif char == '/':
            result = num_1 / num_2
        stack.append(result)

answer = stack.pop()
print(f'{answer:.2f}')