# 처음에 짠 코드

def solution(n):
    answer = 0
    list1 = []
    if n < 3:
        list1.append(n)
    else:
        while (n >= 3):
            list1.append(int(n % 3))    
            if (n//3 < 3):
                list1.append(int(n // 3))
            n /= 3
    for i in range(len(list1)):
        answer += (pow(3, i) * list1[::-1][i]) 
    print(answer)        
    return answer

# 첫번째 코드 효율적으로 수정

# def solution(n):
#     answer = 0
#     list1 = []
#     while (n > 0):
#         list1.append(int(n % 3))
#         n = int(n // 3)
#     for i in range(len(list1)):
#         answer += (pow(3, i) * list1[::-1][i])        
#     return answer

# 다른 사람 코드

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3
#         print(tmp)
#     answer = int(tmp, 3)
#     print(answer)
#     return answer