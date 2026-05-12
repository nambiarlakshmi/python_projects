def first_bit_place(n):
    place = 1 
    while n > 0:
        if n & 1 == 1:
            return place
        n= n >> 1
        place += 1
    
num = first_bit_place(5)
print(num)