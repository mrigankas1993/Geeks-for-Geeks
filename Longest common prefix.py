def longestCommonPrefix(str1, str2):
    count = 0
    trigger = True
    result = []
    for j in range(1,len(str1) + 1):
        if str1[:j] in str2:
            if trigger == True:
                result.append(j - 1)
                trigger = False
            count += 1
    result.append(count - 1)
    if count == 0:
        return [-1,-1]
    else:
        return result
str1 = "practicegeeks"
str2 = "coderpractice"
print(longestCommonPrefix(str1, str2))
                
