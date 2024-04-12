nums = {'a':'1', 'b':'2', 'c':'3'}

print(id(nums))
print(nums)

nums['a']='2'
nums.setdefault('d', 4)
nums1=nums
print(id(nums))
print(nums)
print(id(nums1))
print(nums1)