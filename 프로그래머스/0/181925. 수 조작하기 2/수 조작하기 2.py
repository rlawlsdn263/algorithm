def solution(numLog):
    commands = []

    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]

        if diff == 1:
            commands.append("w")
        elif diff == -1:
            commands.append("s")
        elif diff == 10:
            commands.append("d")
        elif diff == -10:
            commands.append("a")

    return "".join(commands)