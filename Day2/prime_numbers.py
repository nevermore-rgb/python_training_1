def is_prime( n: int ):
    list = [2,3,5,7,11]
    
    if n < 2:
        return False
    
    for item in list:
        if ( n == item ):
            continue
        elif ( n % item == 0 ):
            return False
    return True

n = int(input("Enter a number: "))

counter= 0

for y in range(1, n+1):
    if (is_prime(y)):
        counter += 1
print(counter)
