"""
Have method to calculate factorial of a number.
"""
def factorial( n ):
    """
    method to calculate factorial of a number
    """
    result  =  1

    for i in range( 1 , n + 1 ):

        result  =  result * i

    return result


if __name__  ==  "__main__" :

    INPUT_NUMBER  =  5

    print( "Factorial of" , INPUT_NUMBER , "is" , factorial( INPUT_NUMBER ) )
