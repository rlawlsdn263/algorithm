def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    # 열의 수가 행의 수보다 많을 경우, 행을 추가
    if cols > rows:
        for _ in range(cols - rows):
            arr.append([0] * cols)
    # 행의 수가 열의 수보다 많을 경우, 각 행에 0을 추가
    elif rows > cols:
        for row in arr:
            row.extend([0] * (rows - cols))
            
    return arr