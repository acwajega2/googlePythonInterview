nums = [-1, 0, 1, 2, -1, -4]
result = []
nums.sort()
r=len(nums)-1
for i in range(len(nums)-2):
    l = i + 1  # we don't want l and i to be the same value.
               # for each value of i, l starts one greater
               # and increments from there.
    while (l < r):
        sum_ = nums[i] + nums[l] + nums[r]
        if (sum_ < 0):
            l = l + 1
        if (sum_ > 0):
            r = r - 1
        if not sum_:  # 0 is False in a boolean context
            result.append([nums[i],nums[l],nums[r]])
            l = l + 1  # increment l when we find a combination that works

>>> result
[[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]]