for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        if number % 3 == 0 and number % 5 == 0:
            print('fizbuzz')
        elif number % 3 == 0:
            print('fizz')
        else:
            print('buzz')
    else:
        print(number)
