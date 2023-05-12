def solution(nums):
    pick = len(nums)/2
    poketmon = set(nums)
    cnt = 0
    if pick >= len(poketmon):
        cnt = len(poketmon)
    else:
        cnt = pick
    return cnt