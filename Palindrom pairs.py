# find if any palindrom pairs are possible by concatinating any two elements of the array and rerurn the index number which could be concat to form the palindrome sequence
arr = ['geekf', "geeks", "or", "keeg", "abc", "bc"]
hash_map = {}
for j in range(len(arr)):
    hash_map[arr[j]] = j
def palindrom_pair(arr, hash_map):
    for i in range(len(arr)):
        f = len(arr[i])
        for j in range(1,f):
            left = arr[i][:j]
            right = arr[i][j:f]
            if left[::-1] in hash_map and right == right[::-1]:
                return "The valid palindrom pair is index" + " " + str(i) + " , " + str(hash_map[left[::-1]])

                                                                                  
            if right[::-1] in hash_map and left == left[::-1]:
                print("yes")
                return "The valid palindrom pair is index" + str(i) + " , " + str(hash_map[right[::-1]])
            
c = palindrom_pair(arr, hash_map)
print(c)


            
                                                                                  
                                                                                
            
            
        
        
    
    




