# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the **type** of fruit the `ith` tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# - You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.
# - Starting from any tree of your choice, you must pick **exactly one fruit** from **every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

# Given the integer array `fruits`, return *the **maximum** number of fruits you can pick*.


# 1. 
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# 2. 
# Input: fruits = [0,1,2,2]
# Output: 3

# 3.
# Input: fruits = [1,2,3,2,2]
# Output: 4

def solution(input):
    
    
    
    def helper(input):
        visited = set()
        result = 0
        for fruit in input:
            if fruit not in visited and len(visited)<2:
                result +=1
                visited.add(fruit)
            elif fruit in visited:
                result+=1
            else:
                break
        #print(result)
        return result
    
    res = 0
    for i in range(len(input)):
        res = max(res,helper(input[i:]))
    return res
        
        
    
                
print(solution([1,2,1]))
print(solution([0,1,2,2]))
print(solution([1,2,3,2,2]))