# 이러한 for문 출력 방식을 사용하여 다음과 같이 구구단 5단을 반복문으로 출력하는 프로그램을 작성해 보세요.
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45

# for i in [1,2,3,4,5,6,7,8,9] :
#     print("5 *",i,"=",i*5)

# score 리스트에 있는 점수를 꺼내서 70점 이상이면 합격, 이하면 불합격 하도록 출력하는 프로그램을 작성하세요.
# 1 번 학생 점수는 90 이고 합격
# 2 번 학생 점수는 35 이고 불합격
# 3 번 학생 점수는 75 이고 합격
# 4 번 학생 점수는 69 이고 불합격
# 5 번 학생 점수는 80 이고 합격

# score = [90, 35, 75, 69, 80]
# num = 0

# for s in score :
#     num += 1
#     if s >= 70 :
#         print(num,"번 학생 점수는",s,"이고 합격")
#     else :
#         print(num,"번 학생 점수는",s,"이고 불합격")

# for i in range(100) : #0~99번
#     print("Hello World")

# for i in range(3) : #0~2까지 출력
#     print(i)

# 시작하는 숫자와 끝나는 숫자 지정하기
# for i in range(5,10) :
#     print(i, end=" ")

# 증가폭 사용하기
# for i in range (0,10,2) :
#     print(i,end=" ")

# 숫자 감소
# for i in range (10, 0, -1) :
#     print(i, end=" ")

# 순서 뒤집어서 사용
# for i in reversed(range(3)) :
#     print(i, end=" ")

# for문을 이용하여 1부터 10까지 모든 수의 합을 구하는 프로그램을 작성해보세요.
# sum = 0
# for i in range(11) :
#     sum = sum + i
# print(sum)

# 입력한 횟수대로 반복하는 프로그램을 작성해보세요.
# c = int(input("횟수: "))
# for i in range(c) :
#     print("H",i)

# 다음과 같이 정수 하나를 입력 받아 1부터 해당 숫자까지 더하는 프로그램을 작성해 보세요.
# 어디까지 계산할까요: 10
# 1부터 10 까지의 정수의 합: 55
# max = int(input("어디까지 계산할까요: "))
# sum = 0
# for i in range(1, max+1) :
#     sum = sum + i
# print("1부터",max,"까지의 정수의 합:",sum)

# 다음과 같이 구구단 단수를 입력 받아 해당 단을 반복문으로 출력하는 프로그램을 작성해 보세요.
# 단: 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45

# dan = int(input("단: "))
# for i in range(1,10) :
#     print(dan,"*",i,"=",dan*i)

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 짝수를 오름차순으로 출력하는 프로그램을 작성하세요. (for문 사용)
# 양의 정수 입력: 19
# 2 4 6 8 10 12 14 16 18
# 양의 정수 입력: 10
# 2 4 6 8 10 

# n = int(input("양의 정수 입력: "))
# for i in range(2, n+1, 2) :
#     print(i, end=" ")

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 3의 배수를 출력하는 프로그램을 작성하세요.
#   (for문 사용)
# n = int(input("양의 정수 입력: "))
# ans = 3
# for i in range (n) :
#     print(ans)
#     ans += 3

# 다음과 같이 정수 두 개를 입력 받아, 둘 중 큰 수에서 작은 수 사이를 카운트 다운 하는 프로그램을 작성하세요. (for문 사용)
# 정수 입력: 8
# 정수 입력: 3
# 8
# 7
# 6
# 5
# 4
# 3

# n1 = int(input("정수 입력: "))
# n2 = int(input("정수 입력: "))

# if n1 > n2 :
#     upper = n1
#     lower = n2
# else :
#     upper = n2
#     lower = n1
# for i in range(upper,lower-1,-1) :
#     print(i)

# 다음과 같이 정수 두 개를 입력 받아, 둘 중 작은 수 부터 큰 수까지의 합을 출력하는 프로그램을 작성하세요. (for문 사용)
# 정수 입력: 5
# 정수 입력: 10
# 5 에서 10 까지 더하면 45

# n1 = int(input("정수 입력: "))
# n2 = int(input("정수 입력: "))
# sum = 0

# if n1 > n2 :
#     upper = n1
#     lower = n2
# else :
#     upper = n2
#     lower = n1

# for i in range(lower, upper+1) :
#     sum = sum + i
# print(sum)

# for i in range(10):
#     print(i, end=' ')
#     i = 100 # 반복문 변수에 강제로 값 변경

# i = 0
# while True :
#     print(i, end= " ")
#     i += 1
#     if i == 10 :
#         break
# print(end="\n")
# print("무한루프 탈출")

# for i in range(1000) :
#     print(i, end= " ")
#     i += 1
#     if i == 10 :
#         break
# print(end="\n")
# print("무한 루프 탈출")

# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0 :
#         continue
#     print(i, end=" ")

# for i in range(10) :
#     if i % 2 == 0 :
#         continue
#     print(i, end=" ")

# for i in range(3) :
#     for j in range(2) :
#         print(j, end=" ")
#     print()

# 사각형 모양 출력하기
# for i in range(3) :
#     for j in range(5) :
#         print("*",end="")
#     print()

# 입력 받아 사각형 출력
# w = int(input("가로: "))
# h = int(input("세로: "))
# for i in range(h) :
#     for j in range(w) :
#         print("*",end="")
#     print()

# 다음과 같이 층수를 입력 받아 아래와 같은 직각삼각형을 그리는 프로그램을 작성하세요.
# 층수: 5
# *
# **
# ***
# ****
# *****

# 층수 = int(input("층수:"))
# for i in range(층수) :
#     for j in range(i+1) :
#         print("*",end="")
#     print()

# 다음과 같이 층수를 입력 받아 아래와 같은 직각삼각형을 그리는 프로그램을 작성하세요.
# 층수: 5
# *****
# ****
# ***
# **
# *

# 층수 = int(input("층수:"))
# for i in range((층수)) :
#     for j in range(층수-i) :
#         print("*",end="")
#     print()

# 중첩 for문을 사용하여 2단부터 9단까지의 구구단을 모두 출력하세요.
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# …

# …
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81

# for i in range(2, 10) :
#     for j in range(1,10) :
#         print(i,"*",j,"=",i*j)
#     print()