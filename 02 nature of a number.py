#----------2 Program to check if a number is positive, negative or zero ------------
while True:
    try:
        num = input('Enter a number to check its nature : ')
        num = float(num)
        if num > 0:
            print('positive')
        elif num < 0:
            print('negative')
        elif num == 0:
            print('zero')
        break
    except:
        print('Invalid entry.')
