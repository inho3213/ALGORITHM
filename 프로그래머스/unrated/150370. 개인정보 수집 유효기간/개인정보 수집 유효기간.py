def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int, today.split('.'))
    date = year*12*28 + month*28 + day
    
    term_dic = {}
    for i in terms:
        term, term_day = i.split()
        term_day = int(term_day)*28
        term_dic[term] = term_day
    
    
    for i in range(len(privacies)):
        dd, tt = privacies[i].split()
        year1, month1, day1 = map(int, dd.split('.'))
        date1 = year1*12*28 + month1*28 + day1
        if date1 + term_dic[tt] <= date :
            answer.append(i+1)
    return answer

