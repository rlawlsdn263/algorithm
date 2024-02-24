def solution(myStr):
    # 'a', 'b', 'c'를 구분자로 사용해 문자열 나누기
    split_str = []
    current_str = ""
    for char in myStr:
        if char in ['a', 'b', 'c']:
            if current_str:  # 현재 문자열이 비어있지 않다면 추가
                split_str.append(current_str)
                current_str = ""
        else:
            current_str += char
    if current_str:  # 마지막 부분 문자열 추가
        split_str.append(current_str)
    
    # 결과가 빈 배열인 경우 "EMPTY"를 포함하는 배열 반환
    return split_str if split_str else ["EMPTY"]