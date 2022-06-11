
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
