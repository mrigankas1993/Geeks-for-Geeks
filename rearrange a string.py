# Rearrange a string
'''
  Given a string containing uppercase alphabets and integer digits (from 0 to 9),
  the task is to print the alphabets in the lexicographical order followed by the sum of digits.
'''
string = 'GD3EANJ3'
# using a list as a stack with .append() and .pop()
stack = []
for i in string:
    stack.append(i)
stack.sort()
summation = 0
string = ''
while len(stack) > 0:
    c = stack.pop(0)
    if c.isdigit() == True:
        summation += int(c)
    else:
        string += c
summation = str(summation)
string = string + summation
print(string)

    
        
    
        


