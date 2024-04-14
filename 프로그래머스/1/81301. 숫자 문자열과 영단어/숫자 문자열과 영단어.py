def solution(s):
    answer = ""
    comb = ""

    numbers = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for num in s:
        if num.isalpha():
            comb += num
        else:
            answer += num

        if comb in numbers:
            answer += numbers[comb]
            comb = ""

    return int(answer)
