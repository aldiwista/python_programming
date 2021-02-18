def swap_bits(x, i, j):
    if ((x>>i)&1) != ((x>>j)&1):
        bit_mask = (1<<i)|(1<<j)
        return (x^bit_mask)
    return x

x = input("Input a Decimal Value :")
i = input("Choose the position of the first bit : ")
j = input("Choose the position of the second bit :")
print(f'The result of swapping bits {i} and {j} in {x} is : {swap_bits(int(x),int(i),int(j))}')