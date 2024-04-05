def solution(s):
    r = []
    answer = {}

    for idx, chr in enumerate(s):
        if chr not in answer:
            answer[chr] = {'i': idx, 'v': -1}
            r.append(-1)
        else: 
            answer[chr] = {'i': idx, 'v': idx - answer[chr]['i']}
            r.append(answer[chr]['v'])

    return r