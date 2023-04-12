def gcd(a, b):

    while a != 0 and b != 0:

        if a > b:

            a = a % b

        else:

            b = b % a


    print('Наибольший делитель:', a + b)





gcd(4782, 698)
