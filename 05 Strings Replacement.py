age = 32
print("I am {}".format(age))

#INDEXES START FROM 0!
print("this sentence got {0} variable elements {1}.".format(2, "printed"))
print('\n')


for i in range(1,13):   #colon and number to determin how many caracters represents value
    print('No. {0:2} square is {1:4} and cube is {2:4}'.format(i, i ** 2, i ** 3)) #exponem operator 'dobleAsterix rise to power

print()
for i in range(1,13):   #colon and <right >lrft ^center
    print('No. {0:2} square is {1:^4} and cube is {2:>4}'.format(i, i ** 2, i ** 3)) #exponem operator 'dobleAsterix rise to power

print()
print("Pi is more less about {0:20}".format(22 /7))
print("Pi is more less about {0:20f}".format(22 /7))
print("Pi is more less about {0:20.50f}".format(22 /7))
print("Pi is more less about {0:50.50f}".format(22 /7))
print("Pi is more less about {0:<60.50f}".format(22 /7))
print("Pi is more less about {0:<70.54f}".format(22 /7))