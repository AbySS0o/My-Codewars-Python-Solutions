def solution(number):
    number -= 1
    answer = 0
    
    if number <= 0:
        return 0
    
    while number != 0:
        if number % 3 == 0:
            answer += number
        elif number % 5 == 0:
            answer += number
        number -= 1
    
    return answer
  