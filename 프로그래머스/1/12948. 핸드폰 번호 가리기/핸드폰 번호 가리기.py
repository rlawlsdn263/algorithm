def solution(phone_number):
    return "".join(['*' for x in phone_number[0:len(phone_number) - 4]]) + phone_number[len(phone_number) - 4:]