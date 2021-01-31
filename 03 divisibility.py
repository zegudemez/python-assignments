#------------3 Program to check whether a number is completely divisible by another number ----------
while True:
    try:
        num2 = input('Enter dividend : ')
        num1 = input('Enter divisor : ')
        num1 = int(num1)
        num2 = int(num2)
        if num2 % num1 == 0:
            print('The two numbers are completely divisible by eachother.')
        else:
            print('The two numbers are not completely divisible by eachother.')
            remainder = num2 % num1
            remainder = str(remainder)
            print('You should subtract ' + remainder + ' this amount from dividend.')
        break
    except:
        print('Invalid entry. Enter integer values.')
