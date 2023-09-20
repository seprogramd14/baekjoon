def solution(my_string, alp):
    return my_string.replace(alp, alp.upper()) if alp in my_string else my_string