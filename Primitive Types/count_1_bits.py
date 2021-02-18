#Author : Aldi Wista Fadhilah
#This program calculates the number of bit 1 in the binary value
def count_bits(x):
    num_bits = 0
    while x : 
        num_bits += x & 1 #Operates AND operation between LSB and '1'
        x >>= 1 #Shift the bit by one to the right. To illustrate 1010 becomes 0101
    return num_bits

x = input("Input a DECIMAL NUMBER : ")
print(f'The number of bit 1 in {x} is {count_bits(int(x))}')