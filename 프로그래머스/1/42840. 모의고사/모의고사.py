def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    result = []

    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            scores[2] += 1

    max_score = max(scores)
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i+1)

    return result