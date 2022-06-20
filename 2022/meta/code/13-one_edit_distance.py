
# An edit between two strings is one of the following changes. 
 

# Add a character
# Delete a character
# Change a character
# Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit. 
# Expected time complexity is O(m+n) where m and n are lengths of two strings. 

def oneEdit(s1, s2):
    # if abs(len(s1) - len(s2)) > 1:
    #     return False
    # distance = 0
    # i, j = 0, 0
    # while i < len(s1) and j < len(s2):
    #     if s1[i] != s2[j]:
    #         distance += 1
    #         if distance > 1:
    #             return False
    #         if len(s1) == len(s2):
    #             i += 1
    #             j += 1
    #             continue
    #         if len(s1) < len(s2):
    #             j += 1
    #             continue
    #         if len(s1) > len(s2):
    #             i += 1
    #     else:
    #         i += 1
    #         j += 1
    # return True
    
# m = len(s)
#         n = len(t)
       
        
#         if s == t:
#             return 0
#         if (m*n == 0 and m+n ==1):
#             return 1
#         dp = [[0] * (n+1) for _ in range(m+1)]
#         for i in range(m+1):
#             dp[i][0] = i
#         for j in range(n+1):
#             dp[0][j] = j
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 insert = dp[i-1][j] +1
#                 replace = dp[i-1][j-1] 
#                 delete = dp[i][j-1] +1
#                 if s[i-1] != t[j-1]:
#                     replace +=1
#                 dp[i][j] = min(insert, replace,delete)
                    
#         return dp[-1][-1] ==1
    
    i , j = 0 , 0
    distance  = 0
    if abs(len(s1) - len(s2) )>1:
        return False
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i +=1
            j +=1
        else:
            distance +=1
            if distance >1:
                return False
            if len(s1) == len(s2):
                i +=1
                j +=1
                continue
            if len(s1) > len(s2):
                i+=1
                continue
            if len(s1) < len(s2):
                j +=1
        return True
            


if __name__ == '__main__':
    print(oneEdit("peaks", "geeks")) # True
    print(oneEdit("peaks", "gaeks")) # False
    print(oneEdit("steve", "michael"))
