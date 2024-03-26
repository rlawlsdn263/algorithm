def solution(s):
    array = []

    splitArr = s.split(" ")
    for split in splitArr:
        word = ""
        for i, v in enumerate(split):
            if i % 2 == 0:
                word += v.upper()
            else: 
                word += v.lower()
        array.append(word)

    return " ".join(array)