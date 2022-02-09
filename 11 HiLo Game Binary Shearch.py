#write computer to guess any no in range 0-1000 with 10 guesses
#.casefold()
low = 1
high = 1000


input("Think of a number from {} to {}: "
      "\n Hit ENTER when You ready.".format(low, high))

while low != high:
    answer = low + (high - low) // 2
    validate = input("{} - (R)ight, (L)ower, (H)igher: ".format(answer)).casefold()
    if validate == 'h':
        low = answer + 1
    elif validate == 'l':
        high = answer - 1
    elif validate == 'r':
        print(" I am champion \_('')_/ thank You ")
        break
    else:
        print(" Type R  L  H ")


# high validate = input("{} - (R)ight, (L)ower, (H)igher: ".format(answer).casefold())
# while validate != 'r':
#     if validate == 'h':
#         low = answer
#         answer = (low + high) //2
#         validate = input("{} - (R)ight, (L)ower, (H)igher: ".format(answer).casefold())
#     elif validate == 'l':
#         high = answer
#         answer = ((high - low) // 2 ) + low
#         validate = input("{} - (R)ight, (L)ower, (H)igher: ".format(answer))
# print(" I am champion \_('')_/ thank You ")

