# Q.4 Write program to create an 1-D NumPy array named <<Your Name>> with evenly
# spaced 25 numbers from 10 to 100 using linspace(). 

import numpy as np

MOHAN=np.linspace(10,100,25)
print(f"Array formed is : \n {MOHAN}")
print('\n')


# Print the dimensions of the array,shape, total elements, the data type of each element 
# and total number of bytes consumed by the array. 

print(f"Dimentions of the array is : {MOHAN.ndim}")
print('\n')

print(f"Shape of the array is : {MOHAN.shape}")
print('\n')

print(f"Size of the array is : {MOHAN.size}")
print('\n')

print(f"Datatype of each element of the array is : {MOHAN.dtype}")
print('\n')

print(f"Total number of bytes consumed by the array is : {MOHAN.nbytes}")
print('\n')

# Find the transpose of this array using reshape() attribute. 

MOHAN_reshaped=MOHAN.reshape(25,1)
print(f"transpose of the array is : {MOHAN_reshaped}")
print('\n')


# Can we do the same with T attribute?

print(f"transpose of the array is : {MOHAN_reshaped.T}")
print('\n')
