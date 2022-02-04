# Find Position of set bit

def findPosition(N):
    if N == 0:
        return -1
    binary = str(bin(N))
    binary = binary[2:]
    binary = binary[::-1]
    if binary.count('1') > 1:
        return -1
    else:
        position = binary.index('1')
        return (position + 1)
print(findPosition(7))

    
    
    
    
    
