nums = [1,2,3,4]
size = len(nums)
if size == 0:
    print(nums)
else:
    nums.insert(0,nums[-1])
    nums.pop()
    print(nums)
