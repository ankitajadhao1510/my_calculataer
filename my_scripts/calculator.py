# operation = int(input(" 1. addition, 2. subtraction, 3. multipltion, 4. divied :- \n"))
# if operation > 4:
#     print('invalid no')
# elif operation < 5:
#     num1 = float(input('1st no:- '))
#     num2 = float(input('2nd no:- '))
#     if operation == 1:
#         num = num1 + num2
#         print(num)
#     elif operation == 2:
#         num = num1 - num2
#         print(num)
#     elif operation == 3:
#         num = num1 * num2
#         print(num)
#     elif operation == 4:
#         num = num1 // num2
#         print(num)
#(another cal )


# print('''1. addition
#  2. subtraction,
#  3. multipltion,
#  4. divied''')
# while True:
#     choice = int(input(" 1. addition, 2. subtraction, 3. multipltion, 4. divied :- \n"))
#     if choice in (1, 2, 3, 4):
#         num1 = float(input('1st nu:- '))
#         num2 = float(input('2nd nu:- '))
#         if choice == 1:
#             num = num1 + num2
#             print(num)
#         elif choice == 2:
#             num = num1 - num2
#             print(num)
#         elif choice == 3:
#              num = num1 * num2
#              print(num)
#         elif choice == 4:
#             num = num1 // num2
#             print(num)
#         next_cal = input('yes oe no:- \n')
#         if next_cal == 'no':
#             break
#     else:
#         print('invalid no!')
#,,,,,,,,,,,,,,,,,,,,,,,,,,



# print(numbere)
print('''1. addition
 2. subtraction,
 3. multipltion,
 4. divied''')
while True:
    choice = int(input(" 1. addition, 2. subtraction, 3. multipltion, 4. divied :- \n"))
    a = input('no:-').split()
    number = [float(i) for i in a]
    result = 0
    if choice == 1:
        for i in number:
            result += i
    elif choice == 2:
        for i in number:
            result -= i
    elif choice == 3:
        result = 1
        for i in number:
            result *= i
    elif choice == 4:
        result = 1
        for i in number:
            result /= i
    print(result)

    next_no = input('yes or no:- \n')
    if next_no == 'no':
        break
    else:
        print('invalid no')



