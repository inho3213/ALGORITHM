def solution(clothes):
    clo = {}
    answer = 1
    for i in range(len(clothes)):
        if clothes[i][-1] in clo:
            clo[clothes[i][-1]] += 1
        else:
            clo[clothes[i][-1]] = 1
    for value in clo.values():
      answer = answer * (value+1)
    return answer-1