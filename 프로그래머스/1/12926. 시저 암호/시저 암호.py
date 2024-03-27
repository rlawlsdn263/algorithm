def solution(s, n):
    s = list(s) # 문자를 배열로 만들기 쉬운 방법

    for i in range(len(s)):
        if s[i] == " ": continue # 공백이면 무시한다
        corr = ord('A') if s[i].isupper() else ord('a') # 대문자면 ord('A') 아니면 ord('a'), #65 #97
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)

    return "".join(s)