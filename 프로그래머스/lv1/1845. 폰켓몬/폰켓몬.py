def solution(nums):
    maxPick = len(nums) // 2
    count = 0
    picked = []
    for i in range(len(nums)):
        if nums[i] not in picked:
            picked.append(nums[i])
    if len(picked) > maxPick: return maxPick
    return len(picked)
