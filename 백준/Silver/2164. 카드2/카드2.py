from collections import deque


def solution(n):
    # n 크기의 배열을 만든다.
    arr = deque(range(1, n + 1))

    # 0번 인덱스를 제거하고, 그 다음 인덱스를 맨 뒤로 보낸다.
    # while 문으로 값이 나올 때까지 반복한다.
    while len(arr) > 1:
        arr.popleft()
        arr.append(arr.popleft())

    return arr[0]


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print(solution(n))