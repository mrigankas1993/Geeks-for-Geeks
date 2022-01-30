# Reverse words in a given string without reversing the individual words
S = 'i.like.this.program.very.much'
stack = [] # we will use a list to replicate the behaviour of a stack by using pop() and append() methods
def reverse_words(S, stack):
    parts = ''
    ans = ''
    for i in S:
        if i == '.':
            stack.append(parts)
            stack.append('.')
            parts = ''
            continue
        parts += i
    stack.append(parts)
    while len(stack) != 0:
        ans += stack.pop()
    return ans
print(reverse_words(S, stack))
        
            
            
        
