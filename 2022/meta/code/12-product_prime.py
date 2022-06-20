
# given a set of prime numbers return all possible composite numbers from the given set (given numbers included).
# For example :
# Input: [2, 3, 5]
# Output : [1, 2, 3, 5, 6, 10, 15, 30]
def productPrime(nums):
    # if not nums:
    #     return []
    # res = productPrime(nums[1:])
    # return [nums[0]] + res + [i * nums[0] for i in res]
    if not nums:
        return []
    cur = productPrime(nums[1:])
    return [nums[0]] + cur + [nums[0] * i for i in cur]


if __name__ == '__main__':
    print(productPrime([2,7,11]))
