def find_pair(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return (num, target - num)
        seen.add(num)
    return None
