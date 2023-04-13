def gcd(a, b):

    while a != 0 and b != 0:

        if a > b:

            a = a % b

        else:

            b = b % a


<<<<<<< HEAD
    print('Наибольший общий делитель:', a + b)
=======
    print('Наибольший делитель:', a + b)
    print('Их множитель: ',a * b)

>>>>>>> out_2




gcd(4782, 698)
