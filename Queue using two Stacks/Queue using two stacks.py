#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    while len(stack1) != 0:
        c = stack1.pop()
        stack2.append(c)
    stack1.append(x)
    while len(stack2) != 0:
        c = stack2.pop()
        stack1.append(c)
        
        
    
    

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    #code here
    if len(stack1) > 0:
        return stack1.pop()
    else:
        return -1
