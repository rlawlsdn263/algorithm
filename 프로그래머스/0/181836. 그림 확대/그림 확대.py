def solution(picture, k):
    enlarged_picture = []
    for row in picture:
        # Create a new row by repeating each character k times
        new_row = ''.join(char * k for char in row)
        # Repeat the new row k times and add to the enlarged picture
        for _ in range(k):
            enlarged_picture.append(new_row)
    return enlarged_picture