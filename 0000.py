# data = [2, 3.4, 45, 100, 101, 103, 122, 179, 164, 188, 199, 200, 307, 399]
# print(data)
#
#
#
#
#
#
# numbers = '2,332,084;673/628:7'
# separators = numbers[1::4]
# print(separators)
# values = "".join(char
#                  if char not in separators
#                  else
#                  '' for char in numbers).split()
# print(values)
# print([int(val) for val in values])
#numb = ['22,33,44']
numb = [input('Type 3 numbers separated with coma: ')]
for a in numb:
    numbers = a.split(',')
for a in range(len(numbers)):
    numbers[a] = int(numbers[a])
suma = numbers[0] + numbers[1] - numbers[2]
print('a + b - c = {}'.format(suma))


#print(numbers)

# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)