# Encrypt the string - 2
hexa = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D',14 : 'E', 15 : 'F'}
def encrypt(string):
    dicty = {}
    encrypted_string = ''
    for j in string:
        if j not in dicty:
            dicty[j] = 1
        else:
            dicty[j] += 1
    for e in dicty.keys():
        num = dicty[e]
        hexf = ""
        while num != 0:
            c = num % 16
            num = num // 16
            if c > 9:
                hexf += hexa[c].lower()
            else:
                hexf += str(c)
        encrypted_string += (e + hexf[::-1])
    return encrypted_string[::-1]
print(encrypt('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
        
        
    
    
    
