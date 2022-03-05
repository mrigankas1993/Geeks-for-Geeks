# to be removed to make two strings anagram
def remAnagram(str1,str2):
    
    #add code here
    hash1 = {}
    hash2 = {}
    for j in str1:
        if j not in hash1:
            hash1[j] = 1
        else:
            hash1[j] += 1
    for i in str2:
        if i not in hash2:
            hash2[i] = 1
        else:
            hash2[i] += 1 
    c = 0
    for j in hash1:
        if j not in hash2:
            c += hash1[j]
            continue
        if hash1[j] <= hash2[j]:
            pass
        if hash1[j] > hash2[j]:
            c += hash1[j] - hash2[j]
    for i in hash2:
        if i not in hash1:
            c += hash2[i]
            continue
        if hash2[i] <= hash1[i]:
            continue
        if hash2[i] > hash1[i]:
            c += hash2[i] - hash1[i]
    return c
        
          
c = 'basgadhbfgvhads'
d = 'sjdhgvbjdsbhvbvd'
print(remAnagram(c,d))
    








