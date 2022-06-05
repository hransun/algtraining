

def productPrime(nums):
    if not nums:
        return []
    res = productPrime(nums[1:])
    return [nums[0]] + res + [i * nums[0] for i in res]


if __name__ == '__main__':
    print(productPrime([2,7,11]))
