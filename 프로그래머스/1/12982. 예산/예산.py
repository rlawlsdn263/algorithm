def solution(d, budget):
    count = 0
        
    for num in sorted(d):
        budget -= num
        if budget < 0:
            break
        count += 1
            
    return count