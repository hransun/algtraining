# Friends Of Appropriate Ages


# class Solution(object):
#     def numFriendRequests(self, ages):
#         """
#         :type ages: List[int]
#         :rtype: int
#         """
#         left, right = 0 , 0
#         ans = 0
#         ages.sort()
#         n = len(ages)
#         for age in ages:
#             if age < 15:
#                 continue
#             while ages[left] <= 0.5 * age +7:
#                 left +=1
#             while right +1 < n and ages[right+1] <=age:
#                 right +=1
#             ans += right - left
#         return ans 
def numFriendRequests(ages):
    ages_count = [0] * 121
    for age in ages:
        ages_count[age] += 1
    result = 0
    print(ages_count)
    for age in ages:
        lower_bound = 0.5 * age + 7
        upper_bound = age + 1 if age >= 100 else min(age + 1, 101)
        result += sum(ages_count[int(lower_bound+1): upper_bound])
        print(int(lower_bound+1), upper_bound)
        if ages_count[age] > 0 and int(lower_bound+1) <= age < upper_bound:
            result -= 1
    return result


if __name__ == '__main__':
    print(numFriendRequests([108,115,5,24,82]))
