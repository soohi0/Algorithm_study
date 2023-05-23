def solution(a):
    min_val = min(a)
    left, right = 0, len(a)-1
    left_min, right_min = float('inf'), float('inf')
    cnt = 0
    while left < right:
        if a[left] < left_min:
            left_min = a[left]
            cnt += 1
        if a[right] < right_min:
            right_min = a[right]
            cnt += 1
            
        if a[left] != min_val:
            left += 1
        if a[right] != min_val:
            right -= 1
    
    return cnt