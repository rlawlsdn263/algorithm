def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])  # 도감에 수록된 포켓몬의 수
    M = int(data[1])  # 맞춰야 하는 문제의 수
    
    pokemons_by_number = {}  # 번호 -> 이름
    pokemons_by_name = {}  # 이름 -> 번호
    
    index = 2  # data 배열에서 시작 인덱스
    for i in range(1, N + 1):
        name = data[index]
        pokemons_by_number[str(i)] = name
        pokemons_by_name[name] = str(i)
        index += 1
    
    results = []
    for j in range(M):
        query = data[index]
        if query.isdigit():  # 숫자인 경우 번호로 이름 찾기
            results.append(pokemons_by_number[query])
        else:  # 문자열인 경우 이름으로 번호 찾기
            results.append(pokemons_by_name[query])
        index += 1
    
    # 결과 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
