def sliding_window(nums, k):
    res = [max(nums[:k])]
    for i in range(k-1, len(nums)):
        if (res[-1] < nums[i]):
            res.append(nums[i])
        else:
            res.append(max(nums[i-k+1:i+1]))
    return res


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
print(sliding_window(num_list, 3))
