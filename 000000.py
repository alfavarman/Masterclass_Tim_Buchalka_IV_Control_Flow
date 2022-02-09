data = [2, 3.4, 45, 100, 101, 103, 122, 179, 164, 188, 307, 399]
print(data)

min_value = 100
max_value = 200

slice_1 = 0

# for index, value in enumerate(data):
#     if value >= min_value:
#         del data[:index]
#         break
# print(data)
### DONT REMOVE VALU INSIDE LOOP!

for index, value in enumerate(data):
    if value >= min_value:
        slice_1 = index
        break
del data[:slice_1]
print(data)

slice_2 = 0
for index, value in enumerate(data[::-1]):
    if value < max_value:
        slice_2 = - index
        break
del data[slice_2:]
print(data)