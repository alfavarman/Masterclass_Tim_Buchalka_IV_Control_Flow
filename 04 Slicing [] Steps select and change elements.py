#Select separators from string
#create empty string, add char changed by if
numbers = "245,367;999 832:102"
separators = (numbers[3::4])
values = "".join(character if character not in separators else "" for character in numbers).split()
print([int(character) for character in values])


# Challange: slice QPO, edcba, last 8 in reverse order

letters = 'abcdefghijklmnopqrstuvwxyz'
backwards = letters[::-1]  #SLICING IDIOM - REVELSAL
print(letters[:]) # print copy

print(backwards)
print(letters[-10:13:-1])
print(letters[-22::-1])
print(letters[25:-9:-1])

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])