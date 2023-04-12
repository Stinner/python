import HEAD as HEAD


def gcd(a, b):

    while a != 0 and b != 0:

        if a > b:

            a = a % b

        else:

            b = b % a


<<<<<<< HEAD

    print('Наибольший делитель:', a + b)

=======
    print('Наибольший делитель:', a + b )
>>>>>>> out

    print('a')




gcd(4782, 698)
