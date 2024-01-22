def solution(todo_list, finished):
    answer = []
    for list in zip(todo_list, finished):
        if list[1] == False:
            answer.append(list[0])
            
    return answer 