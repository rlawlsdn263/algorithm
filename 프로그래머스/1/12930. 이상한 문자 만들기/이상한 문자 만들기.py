def solution(s):
    answer = ''
    # 단어별로 처리하기 위해 인덱스를 사용합니다.
    index = 0
    for char in s:
        # 공백을 만날 경우 인덱스를 초기화합니다.
        if char == ' ':
            answer += char
            index = 0
        else:
            # 짝수 인덱스의 문자는 대문자로, 홀수 인덱스의 문자는 소문자로 변환합니다.
            if index % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
            index += 1

    return answer