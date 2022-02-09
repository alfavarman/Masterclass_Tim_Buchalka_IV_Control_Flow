numbers = input("Type number")
wrong_input = ""

for i in numbers:
    if not i.isnumeric():
        wrong_input = wrong_input + i

numb = "".join(i if i not in wrong_input else "" for i in numbers)
print(numb)
