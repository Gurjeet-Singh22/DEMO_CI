"""
Have method to check whether a number is prime or not
"""
def is_prime( n ):
    """
    Method to check whether nunber is prime
    """
    if n  <=  1 :
        return False

    for i in range( 2 , n ):

        if n % i  ==  0 :
            return False

    return True


if __name__  ==  "__main__" :

    INPUT_NUMBER  =  17

    if is_prime( INPUT_NUMBER ):
        print( INPUT_NUMBER , "is a prime number." )
    else :
        print( INPUT_NUMBER , "is not a prime number." )
