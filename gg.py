def gcd(a, b):

    while a != 0 and b != 0:

        if a > b:

            a = a % b

        else:

            b = b % a


<<<<<<< Updated upstream
    print('Наибольшее число:', a + b)

=======
    print('Наибольший общий делитель:', a + b)
    print('a')
>>>>>>> Stashed changes


gcd(4782, 698)
