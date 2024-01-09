def solution(arr):
    def f(n):
        if n < 50 and n % 2 == 1:
            return n * 2;
        elif n >= 50 and n % 2 == 0:
            return n / 2;
        else:
            return n;
    
    answer = list(map(f, arr))
    return answer