def solution(brown, yellow):
    total = brown + yellow

    # 약수를 구하는 방법
    for num in range(1, (total + 1)):
        if total % num == 0:
            width = num # 약수 한 개가 가로가 된다
            height = total // num # 넓이 // 가로 = 세로
            
            if (width - 2) * (height - 2) == yellow and width <= height:
                return [height, width]