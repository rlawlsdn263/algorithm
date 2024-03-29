def solution(new_id):
    # 소문자 변환
    answer = new_id.lower()

    # 지정 문자 제외 문자 제거
    filtered = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
            filtered.append(c)

    answer = "".join(filtered)

    # .. -> .로 변환
    while '..' in answer:
        answer = answer.replace('..', '.') # replace는 한 번만 수행되기 때문에 while문으로 실행

    # 양옆의 .을 제거
    answer = answer.strip('.')

    # 아무것도 없으면 'a' 할당
    if answer == '': answer = 'a'

    # 16 이상이면 이상은 삭제 후 마지막 문자 따옴표 삭제
    if len(answer) > 15: answer = answer[:15]
    if answer[-1] == ".": answer = answer[:-1]

    # 반대로 3자 미만이면 마지막 문자 반복해서 3글자 이상
    while len(answer) < 3:
        answer += answer[-1]

    return answer
