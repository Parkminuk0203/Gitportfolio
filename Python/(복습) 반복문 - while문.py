# # 0부터 9까지 출력
# i = 0
# while i < 10 :
#     print(i, end=" ")
#     i += 1

# 반복문을 사용하여 다음과 같이 출력하는 프로그램을 작성하세요.
# 1 번째 Hello World!!
# 2 번째 Hello World!!
# 3 번째 Hello World!!
# 4 번째 Hello World!!
# 5 번째 Hello World!!
# 6 번째 Hello World!!
# 7 번째 Hello World!!

# i = 1
# while i < 8 :
#     print(i,"번째 Hello World!!")
#     i += 1

# 다음과 같이 정수 하나를 입력 받고, 그 수를 단으로 하는 구구단을 출력하세요.
# 출력하고 싶은 단: 7
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# 7 * 4 = 28
# 7 * 5 = 35
# 7 * 6 = 42
# 7 * 7 = 49
# 7 * 8 = 56
# 7 * 9 = 63

# n = int(input("출력하고 싶은 단: "))
# i = 1
# while i < 10 :
#     print(n,"*",i,"=",n*i)
#     i += 1

# # 다음과 같이 양의 정수를 하나 입력 받아, 1부터 그 값까지 카운트 업 하는 프로그램을 작성하세요.
# # 양의 정수 입력: 12
# # 1 2 3 4 5 6 7 8 9 10 11 12 

# n = int(input("양의 정수 입력: "))
# i = 1
# while i <= n :
#     print(i, end=" ")
#     i += 1

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값을 0까지 감소시키면서 카운트 다운하는 프로그램을 작성하세요.
# 양의 정수 입력: 11
# 11 10 9 8 7 6 5 4 3 2 1 0 

# n = int(input("양의 정수 입력: "))
# while n >= 0 :
#     print(n, end=" ")
#     n -= 1

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 짝수를 오름차순으로 출력하는 프로그램을 작성하세요.
# 양의 정수 입력: 19
# 2 4 6 8 10 12 14 16 18

# n = int(input("양의 정수 입력: "))
# i = 2
# while i <= n :
#     print(i, end=" ")
#     i += 2

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 2의 제곱수를 오름차순으로 출력하는 프로그램을 작성하세요.
# 양의 정수 입력: 19
# 2 4 8 16 

# n = int(input("양의 정수 입력: "))
# i = 2
# while i <= n :
#     print(i, end=" ")
#     i *= 2

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 3의 배수를 출력하는 프로그램을 작성하세요
# 양의 정수 입력: 5
# 3
# 6
# 9
# 12
# 15

# n = int(input("양의 정수 입력: "))
# i = 3
# x = 0
# while x < n :
#     print(i, end=" ")
#     x += 1
#     i += 3
     

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 세로로 *을 출력하는 프로그램을 작성하세요.
# 양의 정수 입력: 5
# *
# *
# *
# *
# *

# i = 0
# n = int(input("양의 정수 입력: "))
# while i < n :
#     print("*")
#     i += 1

# 다음과 같이 정수 두 개를 입력 받아, 둘 중 큰 수에서 작은 수 사이를 카운트 다운 하는 프로그램을 작성하세요.
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

# while upper >= lower :
#     print(upper)
#     upper -= 1

# 누적합 구하기
# 양의 정수 입력: 5
# 1 부터 5 까지의 합은 15 입니다
n = int(input("양의 정수 입력: "))
sum = 0
i = 1
while i <= n :
    sum = sum + i
    i += 1
print("1 부터",n,"까지의 합은",sum,"입니다")


# 정수 세 개를 입력 받아 그 합계를 출력하는 프로그램을 작성하세요.
# 정수 입력: 10
# 정수 입력: 20
# 정수 입력: 30
# 합계는 60 입니다.

# i = 0
# sum = 0
# while i < 3:
#     n = int(input("정수 입력: "))
#     sum = sum + n
#     i += 1
# print(sum)

# 정수 하나를 입력 받아 정수의 각 자리수의 합을 출력하는 프로그램을 작성해 보세요.
# 정수 입력: 1234
# 합계는 10 입니다.

# sum = 0
# n = int(input("정수 입력: "))
# while n > 0 :
#     d = n % 10
#     sum = sum+d
#     n = n // 10
# print(sum)

# 정수 하나를 입력 받아 그 자릿수를 출력하는 프로그램을 작성해 보세요.
# 정수 입력: 327463
# 327463 은  6 자리 숫자 입니다.

# n = int(input("정수 입력: "))
# temp = n
# i = 0
# while temp > 0 :
#     temp = temp // 10
#     i += 1
# print(n,"은",i,"자리 숫자 입니다.")

# 성적을 개수 제한없이 입력 받아 평균을 구하는 프로그램을 작성하세요. 음수가 입력되면 종료되어 평균을 출력합니다.
# 종료하려면 음수를 입력하세요
# 성적 입력: 90
# 성적 입력: 80
# 성적 입력: 70
# 성적 입력: -1
# 성적의 평균은 80.000000입니다.

# n = 0
# score = 0
# sum = 0

# print("종료하려면 음수를 입력하세요")
# while score >= 0 :
#     score = int(input("성적 입력: "))
#     if score >= 0 :
#         sum = sum + score
#         n += 1
# if n > 0 :
#     avg = sum / n
# print("성적의 평균은 %f입니다." % avg)

# 최대값 구하기
# max = -1
# n = 0
# while n >= 0 :
#     if n > max :
#         max = n
#     n = int(input("정수 입력: "))
# if max != -1 :
#     print("최대값은",max,"입니다.")

# 1에서 10 사이의 숫자를 임의로 발생 시키기

# import random
# num = random.randint(1,10)
# print(num)

# 주사위를 계속 굴려 3이 나오면 종료하는 하는 프로그램을 작성해 보세요.
# 주사위를 굴렸다.  5 나옴
# 주사위를 굴렸다.  5 나옴
# 주사위를 굴렸다.  1 나옴
# 주사위를 굴렸다.  3 나옴
# 드디어 3 나와서 종료합니다.

# import random
# n = 0
# while n != 3 :
#     n = random.randint(1,6)
#     print("주사위를 굴렸다.",n,"나옴")
# print("드디어 3 나와서 종료합니다.")    

# 랜덤하게 구구단 문제 3개를 출력. 끝나면 몇 문제 맞는지 출력
# 구구단 게임입니다.
# 7 * 9 = 63
# 맞습니다.
# 2 * 8 = 15
# 틀렸습니다.
# 2 * 9 = 18
# 맞습니다.

# 총 3문제 중 2 문제 맞추셨습니다.

# import random
# i = 0
# score = 0
# print("구구단 게임입니다.")
# while i < 3 :
#     num1 = random.randint(1,9)
#     num2 = random.randint(1,9)

#     곱 = num1 * num2
#     print(num1,"*",num2,"=")
#     답 = int(input())

#     i += 1
#     if 답 == 곱 :
#         print("맞습니다")
#         score += 1
#     else :
#         print("틀렸습니다.")
    
# print("총 3문제 중",score,"맞추셨습니다.")

# 가위, 바위, 보 게임을 만들어 봅시다. 랜덤 함수를 이용해서 컴퓨터의 선택을 결정하고, 사용자가 이길 때 까지 반복 합니다.
# 이길 때 까지 계속 합니다.
# 가위, 바위, 보 중 하나를 선택: 보
# 컴퓨터: 가위
# 졌다.
# 가위, 바위, 보 중 하나를 선택: 가위
# 컴퓨터: 가위
# 비겼다.
# 가위, 바위, 보 중 하나를 선택: 바위
# 컴퓨터: 가위
# 이겼다.


# import random
# print("이길 때 까지 계속 합니다.")
# win = False


# while win != True :
#     ans = input("가위, 바위, 보 중 하나를 선택: ")
#     com = random.randint(1,3)
#     print("컴퓨터: ", end ="")
    
#     if com == 1 :
#         print("가위")
#         if ans == "가위" :
#             print("비겼다.")
#         elif ans == "바위" :
#             print("이겼다.")
#             win = True
#         else :
#             print("졌다.")

#     elif com == 2 :
#         print("바위")
#         if ans == "가위" :
#             print("졌다.")
#         elif ans == "바위" :
#             print("비겼다.")
#         else :
#             print("이겼다.")
#             win = True
    
#     elif com == 3 :
#         print("보")
#         if ans == "가위" :
#             print("이겼다.")
#             win = True
#         elif ans == "바위" :
#             print("졌다.")
#         else :
#             print("비겼다.")
