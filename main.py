

def twoSum():
    input_string = input('nums =')
    nums = input_string.split(',')
    result = []

    for i in range(len(nums)):
        nums[i] = int(nums[i])

    target = int(input("target ="))

    check = False
    for i in range(1, len(nums)):
        for j in range(i):
            if (nums[i] + nums[j]) == target:
                check = True
                result.extend([i, j])
                break
        if check:
            break

    print(result)


twoSum()
