#menu = ['choice_1', 'choice_2', 'choice_3', 'choice_4', 'choice_5']
# choice = input('Menu: \n{}'.format(menu))
# menu ="""
# Please select option from list:
# 1. Girl
# 2. Woman
# 3. LadyBoy
# 4. TomBoy
# 0. Exit \n __"""
#
# choice = int(input('{}'.format(menu)))
#
# while True:
#     if 0 <= choice < 5:
#         if choice == 0:
#             print('Thank You')
#             break
#         else:
#             choice = int(input('Selected {} option.'
#                   '\nChoose Option:'.format(choice)))
#
#         #input('Invalid input! Please select option from menu:'
#         #                ' \n{}'.format(menu))

choice = '-'
while choice != '0':
    if choice in '1234':
        print('Selected: {}'.format(choice))
    else:
        print("""
Select From MENU:
                1.\tGirl
                2.\tTomBoy
                3.\tLadyBoy
                4.\tBoy
                0.\tExit""")
    choice = input(" Select:")
print('Good Bye')