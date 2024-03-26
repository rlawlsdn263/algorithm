def solution(strArr):
    return [str.upper() if idx % 2 else str.lower() for idx, str in enumerate(strArr)]