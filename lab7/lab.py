import sys
import math

def baby_step_giant_step(g, h, q):
    # Compute the value of m using the square root of q and add 1
    m = int(q**0.5) + 1
    
    # Initialize an empty dictionary to store logarithmic values
    log = dict()
    
    # Initialize p to 1 and populate the logarithmic dictionary for the first part of the algorithm
    p = 1
    for j in range(m):
        log[p] = j
        p = (p * g) % q
        
    # Calculate the modular inverse of g^(m * (q-2)) % (q-1) to be used in the second part of the algorithm
    inv = pow(g, (m * (q-2)) % (q-1), q)
    
    # Initialize c to the given value of h
    c = h
    
    # Iterate through the second part of the algorithm
    for i in range(m):
        # Check if c is in the logarithmic dictionary
        if c in log:
            # If found, return the result of the algorithm
            return (i * m + log[c]) % q
        else:
            # If not found, update c using the modular inverse
            c = (c * inv) % q

# Take input values for g, h, and q
g, h, q = [int(i) for i in input().split()]

# Print the result of the baby-step giant-step algorithm
print(baby_step_giant_step(g, h, q))
