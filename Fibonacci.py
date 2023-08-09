# Import relevant libraries and packages
import numpy as np


# Retrieve the placement of the number to be calculated in the Fibonacci sequence
place_in_sequence = int(input( "Position in the Fibonacci sequence to calculate:" ))


# Define a function for returning the nth number in a Fibonacci sequence
def fibo_nth( place_in_sequence ):

    # Make array of ones of length place_in_sequence
    fib_seq = np.ones(place_in_sequence)

    # Build a Fibonacci sequence of length place_in_sequence
    for idx,_ in enumerate(fib_seq):

        # Set the first two numbers in the sequence as 0,1
        if (idx == 0) or (idx == 1):
            fib_seq[idx] = idx

        # Calculate all other numbers in the sequence as the sum of the previous 2 numbers
        else:
            fib_seq[idx] = fib_seq[idx-2] + fib_seq[idx-1]

    # Return the final entry in the sequence
    return fib_seq[-1]


# Calculate the desired nth number in the Fibonacci sequence
nth_number = fibo_nth(place_in_sequence)


# Return the number in the Fibonacci sequence corresponding to the given nth placement
print( "The {}th number in the Fibonacci sequence is {}".format(place_in_sequence, nth_number) )




