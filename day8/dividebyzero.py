while True:
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1/num2
    except ValueError:
        print('You must enter two integer')
    except ZeroDivisionError:
        print('Attempted to divide by zero')
    else:
        print(f'{num1}/{num2} = {result:.3f}') #.3f means round up upto 3 decimal
        break