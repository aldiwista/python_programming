#Author : Aldi Wista Fadhilah
#GitHub Account : https://github.com/aldiwista

def reverse_bits(x):
    reverse_bit=0
    temp = []
    for i in range(x.bit_length()):
        temp.append(((x>>i)&1)<<((x.bit_length()-1)-i))
    for b in temp:
        reverse_bit |= b
    return reverse_bit

def decimalToBinary(n): 
    return bin(n).replace("0b", "")

x = input("Input a Decimal Value = ")
result = reverse_bits(int(x))
print(f'Your input is {x}, with binary value :{decimalToBinary(int(x))}')

print(f"The reverse of your input is {result}, with binary value :{decimalToBinary(result)}")


