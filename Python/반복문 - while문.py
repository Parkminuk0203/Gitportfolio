# 반복적(looping) 실행 - 반복문
# 특정 부분을 일정한 횟수만큼 반복 실행하는 반복 제어 구조

# 반복구조
# 같은 처리를 되풀이해서 반복 실행하는 것
# 일괄처리해서 많은 일을 한번에 할 수 있다

# 컴퓨터에서 가장 빠르게 잘 할 수 있는 일
# 같은 결과를 내더라도 가능한 반복을 사용하는 것이
# 알고리즘 적으로 더 효율적일 가능성이 높다!

# while문
# 조건 제어 반복 (특정한 조건이 만족되면 계속 반복)

# for문
# 횟수 제어 반복 (보통 횟수를 정해놓고 반복)

i = 0
while i < 3 :
    print("Hello")
    i = i + 1
#Hello
#Hello
#Hello

# 반복문은 탈출조건을 잘 확인해야 한다
# i = 0
# while i < 3 :
#     print("Hello")
#     # i = i - 1
# 무한 반복됨

i = 0
while i < 10 :
    print(i, end =" ")
    i += 1
#0 1 2 3 4 5 6 7 8 9

i = 1
while i < 8 :
    print(i,"번째 Hello World!!")
    i += 1
# 1 번째 Hello World!!
# 2 번째 Hello World!!
# 3 번째 Hello World!!
# 4 번째 Hello World!!
# 5 번째 Hello World!!
# 6 번째 Hello World!!
# 7 번째 Hello World!!

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

단 = int(input("출력하고 싶은 단: ")) # 7 넣으면
i = 1
while i < 10 :
    print(단, "*", i, "=", 단*i)
    i += 1
#7 * 1 = 7
#7 * 2 = 14
#7 * 3 = 21
#7 * 4 = 28
#7 * 5 = 35
#7 * 6 = 42
#7 * 7 = 49
#7 * 8 = 56
#7 * 9 = 63

# 다음과 같이 양의 정수를 하나 입력 받아, 1부터 그 값까지 카운트 업 하는 프로그램을 작성하세요.
# 양의 정수 입력: 12
# 1 2 3 4 5 6 7 8 9 10 11 12
정수 = int(input("양의 정수 입력: "))
i = 1
while i <= 정수 :
    print(i, end = " ")
    i += 1

# 짝수만 나오게 하고 싶으면
정수 = int(input("양의 정수 입력: "))
i = 0
while i <= 정수 :
    print(i, end = " ")
    i += 2

# 홀수만 나오게 하고 싶으면
정수 = int(input("양의 정수 입력: "))
i = 1
while i <= 정수 :
    if i % 2 == 1 :
        print(i, end = " ")
    i += 1

# 3의 배수만 나오게 하고 싶으면
정수 = int(input("양의 정수 입력: "))
i = 1
while i <= 정수 :
    if i % 3 == 0 :
        print(i, end = " ")
    i += 1

# 3의 배수나 5의 배수
정수 = int(input("양의 정수 입력: "))
i = 1
while i <= 정수 :
    if i % 3 == 0 or i % 5 == 0 :
        print(i, end = " ")
    i += 1

# or 대신 and를 쓰면?
정수 = int(input("양의 정수 입력: "))
i = 1
while i <= 정수 :
    if i % 3 == 0 and i % 5 == 0 : # 3의 배수 그리고 5의 배수, 즉 15의 배수
        print(i, end = " ")
    i += 1

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값을 0까지 감소시키면서 카운트 다운하는 프로그램을 작성하세요.
num = int(input("양의 정수 입력: "))
while num >= 0 :
    print(num , end=" ")
    num -= 1

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 짝수를 오름차순으로 출력하는 프로그램을 작성하세요.
num = int(input("양의 정수 입력: "))
i = 2
while i <= num :
    print(i , end=" ")
    i += 2

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 2의 제곱수를 오름차순으로 출력하는 프로그램을 작성하세요.
num = int(input("양의 정수 입력: "))
i = 2
while i <= num :
    print(i , end=" ")
    i *= 2

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 3의 배수를 출력하는 프로그램을 작성하세요.
num = int(input("양의 정수 입력: "))
i = 0
cnt = 0
while cnt < num :
    cnt += 1
    i += 3
    print(i)

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 세로로 *을 출력하는 프로그램을 작성하세요.
i = 1
정수 = int(input("양의 정수 입력: "))
while i <= 정수 :
    print("*")
    i += 1
# 입력한 정수 만큼 정사각형을 찍으시오.
i = 0
정수 = int(input("양의 정수 입력: "))
while i < 정수:
    i += 1
    print("*" * 정수)

num = int(input("양의 정수 입력: "))
i = 1
cnt = num * num
while i <= cnt :
    print("*", end = "")
    if i % num == 0 :
        print()
    i += 1

# 다음과 같이 정수 두 개를 입력 받아, 둘 중 큰 수에서 작은 수 사이를 카운트 다운 하는 프로그램을 작성하세요.
num1 = int(input("정수 입력: "))
# 정수1를 입력 받음
num2 = int(input("정수 입력: "))
# 정수2를 입력 받음
if num1 > num2 : 
# 만약에 정수1이 정수2보다 크다면
    upper = num1
# upper라는 변수에 정수1의 정수를 대입
    lower = num2
# lower라는 변수에 정수2의 정수를 대입
else :
# 아니면
    upper = num2
# upper라는 변수에 정수2의 정수를 대입
    lower = num1
# lower라는 변수에 정수1의 정수를 대입
i = upper
# upper의 정수를 i의 대입
while i >= lower :
# i의 값이 lower보다 크거나 같으면
    print(i)
    # i를 출력할때마다
    i -= 1
    # i를 1씩 빼라.

# 누적합 구하기
# 1부터 n까지의 합을 구해보자
n = int(input("양의 정수 입력: "))
i = 1
sum = 0
while i <= n :
    sum = sum + i
    i += 1
print("1부터", n, "까지의 합은", sum, "입니다.")

# 정수 세 개를 입력 받아 그 합계를 출력하는 프로그램을 작성하세요.
i = 0
sum = 0
while i < 3 :
    n = int(input("정수 입력: "))
    sum = sum + n
    i += 1
print("합계는", sum, "입니다.")

# 정수 하나를 입력 받아 정수의 각 자리수의 합을 출력하는 프로그램을 작성해 보세요.
# 정수 입력: 1234
# 합계는 10 입니다
sum = 0
n = int(input("정수 입력: "))
while n > 0 :
    data = n % 10
    sum = sum + data
    n = n // 10
print("합계는", sum, "입니다.")

# 정수 하나를 입력 받아 그 자릿수를 출력하는 프로그램을 작성해 보세요.
# 정수 입력: 327463
# 327463 은  6 자리 숫자 입니다.
n = int(input("정수 입력: "))
count = 0
temp = n
while temp > 0 :
    temp = temp // 10
    count += 1
print(n, "은 ", count, "자리 숫자 입니다.")

# 보초값(sentinel)
# 데이터의 끝을 알리는데 사용하는 데이터 값
# 일반적으로 절대로 등장할 수 없는 값으로 선택
# 몇 번을 반복해야 되는지 알 수 없을 때 유용 때
# 보초값이 들어오면 끝으로 판단한다!!

# 성적을 개수 제한없이 입력 받아 평균을 구하는 프로그램을 작성하세요. 음수가 입력되면 종료되어 평균을 출력합니다.
# 종료하려면 음수를 입력하세요
# 성적 입력: 90
# 성적 입력: 80
# 성적 입력: 70
# 성적 입력: -1
# 성적의 평균은 80.000000입니다.
n = 0
sum = 0
score = 0
print("종료하려면 음수를 입력하세요")
# grade가 0이상이면 반복
# 성적을 입력 받아서 합계를 구하고 학생 수를 센다.
while score >= 0 :
    score = int(input("성적 입력: "))
    if score > 0:
        sum = sum + score
        n = n + 1
# 평균을 계산하고 화면에 출력한다.
if n > 0 :
    avg = sum / n
print("성적의 평균은 %f입니다." % avg)

# 최대값 구하기 알고리즘
# 1. 최대값 변수를 선언
# 2. 정수를 입력 받음
# 3. 최대값 변수와 비교
# 4. 최대값 변수보다 입력 받은 값이 크면
#    -> 최대값 변수의 값을 입력 받은 값으로 바꿈
# 5. 입력이 끝날 때 까지 2번 부터 반복

max = -1 # 나올 수 없는 최저값을 임시로 저장
n = int(input("양의 정수 입력: "))
while n >= 0 :
    if n > max :
        max = n
    n = int(input("양의 정수 입력: "))
if max != -1 :
    print("최대값은", max, "입니다.")

# 난수(Random Number)
# 무작위로 나오는 숫자를 난수라고 함
# 파이썬에서 난수를 생성하려면 random 모듈이 필요
# import random
# random모듈의 randint()함수를 사용하면 정수로 난수 발생
# random.randint(시작 값, 끝 값) 

import random
num = random.randint(1,10)
print(num)

import random
num = random.randint(1,6)
while num != 3 :
    num = random.randint(1,6)
    print("주사위를 굴렸다. ",num,"나옴")
print("드디어 3 나와서 종료합니다.")

# 구구단 게임입니다.
# 7 * 9 = 63
# 맞습니다.
# 2 * 8 = 15
# 틀렸습니다.
# 2 * 9 = 18
# 맞습니다.

# 총 3문제 중 2 문제 맞추셨습니다.
# 랜덤하게 구구단 문제 3개를 출력. 끝나면 몇 문제 맞는지 출력

import random
print("구구단 게임입니다.")
i = 0
score = 0

while i < 3 :
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    result = num1 * num2

    print(num1, "*", num2, "= ", end="")
    ans = int(input())

    if ans == result :
        print("맞습니다.")
        score += 1
    else :
        print("틀렸습니다.")
        i += 1
print("\n총 3문제 중", score,"문제 맞추셨습니다. ")

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

import random

print("이길 때 까지 계속 합니다.")

win = False

while win != True :
    ans = input("가위, 바위, 보 중 하나를 선택: ")
    com = random.randint(1,3)
    print("컴퓨터:", end = " ")

    if com == 1 :
        print("가위")
        if ans == "가위" :
            print("비겼다.")
        elif ans == "바위" :
            print("이겼다.")
            win = True
        else :
            print("졌다.")
      
    if com == 2 :
        print("바위")
        if ans == "바위" :
            print("비겼다.")
        elif ans == "보" :
            print("이겼다.")
            win = True
        else :
            print("졌다.")

    if com == 3 :
        print("보")
        if ans == "보" :
            print("비겼다.")
        elif ans == "가위" :
            print("이겼다.")
            win = True
        else :
            print("졌다.")