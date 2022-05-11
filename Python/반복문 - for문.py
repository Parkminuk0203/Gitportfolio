# for문
# for문은 while문보다 활용 빈도가 높으며 반복하는 횟수를 정확히 알고 있을 때 사용
# 중첩 반복문을 사용할 경우에는 while문보다 for문이 더 간결하게 코딩
# 시퀀스에 항목이 남아있으면 변수에 해당 항목을 넣어서 반복시킨다. 없으면 종료
for i in [0,1,2] :
    print(i)
#0
#1
#2
a = [0,1,2]

for i in a :
    print(i)
#0
#1
#2

# 시퀀스 자리에는 리스트나 문자열도 올 수 있다.
for i in "Hello" :
    print(i)
#H
#e
#l
#l
#o

fruits = ('apple', 'orange', 'grape')

for i in fruits :
    print(i)
#apple
#orange
#grape

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

for i in [1,2,3,4,5,6,7,8,9] :
    print("5 *", i, "=", 5*i)

# score 리스트에 있는 점수를 꺼내서 70점 이상이면 합격, 이하면 불합격 하도록 출력하는 프로그램을 작성하세요.
# 1 번 학생 점수는 90 이고 합격
# 2 번 학생 점수는 35 이고 불합격
# 3 번 학생 점수는 75 이고 합격
# 4 번 학생 점수는 69 이고 불합격
# 5 번 학생 점수는 80 이고 합격

score = [90,35,75,69,80]
num = 0

for s in score :
    num += 1
    if s >= 70 :
        print(num, "번 학생 점수는", s, "이고 합격")
    else :
        print(num, "번 학생 점수는", s, "이고 불합격")

# for문과 range()함수는 아주 유용하게 쓰임
# ‘Hello World’ 100번 출력하기
# 0에서 2까지 출력하기

for i in range(100) :
    print('Hello World')
#Hello World 100번 출력
for i in range(3) :
    print( i )
#0
#1
#2

# range() 함수
# 연속된 숫자를 생성하는 함수.
# range(start=0,stop,step=1)
# start 은 시작, stop은 끝, step은 증감값
# start, step은 생략 가능, stop은 반드시 지정 해야함
# start 부터 step-1 까지의 숫자 생성 
# 예를 들어
# range(3) -> 0, 1, 2 이 생성됨
for i in range(3) :
    print( i )
#0
#1
#2
# 이렇게 사용하면 생성된 시퀀스를 for문에서 바로 이용
# 변수 i 에 0 으로 반복, 1로 반복, 2로 반복 하고 끝~
# 사실은
# range()에서 반환하는 것은 range형 객체
# >>> range(3)
# range(0, 3)
# 생성하는 값을 실제로 리스트 자료형으로 보고 싶으면 list() 함수를 사용해야 한다.
# >>> list(range(3))
# [0, 1, 2]

# 시작하는 숫자와 끝나는 숫자 지정하기
for i in range(5, 10) :
    print(i, end=" ")
#5 6 7 8 9

# 증가폭 사용하기
for i in range(0, 10, 2) :
    print(i, end=" ")
#0 2 4 6 8

# 숫자를 감소시키기
for i in range(10, 0) :
    print(i, end=" ")
# 결과 없음

# step에 음수를 넣어줘야 함
for i in range(10, 0, -1) :
    print(i, end=" ")
#10 9 8 7 6 5 4 3 2 1 

# step을 음수로 하는 방법 말고 reversed() 함수를 사용하는 방법도 있음
# range(3)       0, 1, 2 이 생성됨
# reversed(range(3))  2, 1, 0 으로 순서 뒤집음
for i in reversed(range(3)) :
    print(i, end=" ")
#2 1 0 

# for문을 이용하여 1부터 10까지 모든 수의 합을 구하는 프로그램을 작성해보세요.
sum = 0
for i in range(11) :
    sum += i
print(sum)
#55

# 짝수 합
sum = 0
for i in range(0,11,2) :
    sum += i
print(sum)
#30

# 홀수 합
sum = 0
for i in range(1,11,2) :
    sum += i
print(sum)
#25

# 3의 배수
sum = 0
for i in range(0,11,3) :
    sum += i
print(sum)
#18

# 입력한 횟수대로 반복하는 프로그램을 작성해보세요.
count = int(input('반복할 횟수를 입력하세요: '))
for i in range(count):
    print('Hello World', i)

# 다음과 같이 정수 하나를 입력 받아 1부터 해당 숫자까지 더하는 프로그램을 작성해 보세요.
# 어디까지 계산할까요: 10
# 1부터 10 까지의 정수의 합: 55
# 어디까지 계산할까요: 5
# 1부터 5 까지의 정수의 합: 15
i = int(input("어디까지 계산할까요: "))
sum = 0
for i in range(i+1) :
    sum += i
print("1부터", i, "까지의 정수의 합:", sum)

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
dan = int(input("단: "))
for i in range(1,10) :
    print(dan, "*", i, "=", dan * i)

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 짝수를 오름차순으로 출력하는 프로그램을 작성하세요. (for문 사용)
# 양의 정수 입력: 19
# 2 4 6 8 10 12 14 16 18
# 양의 정수 입력: 10
# 2 4 6 8 10 
정수 = int(input("양의 정수 입력: "))
for i in range(2, 정수+1, 2) :
    print(i , end=" ")

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 3의 배수를 출력하는 프로그램을 작성하세요.
# (for문 사용)
# 양의 정수 입력: 5
# 3
# 6
# 9
# 12
# 15
정수 = int(input("양의 정수 입력: "))
ans = 3
for i in range(정수) :
    print(ans)
    ans += 3

# 다음과 같이 정수 두 개를 입력 받아, 둘 중 큰 수에서 작은 수 사이를 카운트 다운 하는 프로그램을 작성하세요. (for문 사용)
# 정수 입력: 8
# 정수 입력: 3
# 8
# 7
# 6
# 5
# 4
# 3

num1 = int(input("정수 입력: "))
num2 = int(input("정수 입력: "))
if num1 > num2 :
    upper = num1
    lower = num2
else :
    upper = num2
    lower = num1 
for i in range(upper, lower-1, -1) :
    print(i)

# 다음과 같이 정수 두 개를 입력 받아, 둘 중 작은 수 부터 큰 수까지의 합을 출력하는 프로그램을 작성하세요. (for문 사용)
# 정수 입력: 5
# 정수 입력: 10
# 5 에서 10 까지 더하면 45
# 정수 입력: 5
# 정수 입력: 4
# 4 에서 5 까지 더하면 9
num1 = int(input("정수 입력: "))
num2 = int(input("정수 입력: "))

if num1 > num2 :
    upper = num1
    lower = num2
else :
    upper = num2
    lower = num1 
sum = 0
for i in range(lower, upper+1) :
    sum += i
print(lower, "에서", upper, "까지 더하면", sum)

# 반복문의 변수에 값을 바꾸면?
for i in range(10):
    print(i, end=' ')
    i = 10 # 반복문 변수에 강제로 값 변경
#0 1 2 3 4 5 6 7 8 9 

# break
# 반복문 동작 중간에 종료하고 나오고 싶을 때 사용 
# 제어흐름 중단

# continue 
# 반복문을 실행할 때 입력 조건을 검사해서 조건에 맞지 않으면 맨 처음으로 다시 돌아가게 할 때 사용
# 제어흐름 유지

# 무한루프와 break로 빠져나가기
# 무한루프 : 반복문의 조건이 항상 참으로 무한히 반복
# while 루프의 조건에 True를 넣으면 무한루프

# while True :
#     계속 반복되는 부분

# 무한루프로 만들어 놓고 특정 조건이 만족하면 break로 빠져나오는 방식으로 사용

# while에서 break 사용하기
i = 0
while True :
    print(i, end = " ")
    i += 1
    if i == 10 :
        break
print(end="\n")
print("무한루프탈출")
#0 1 2 3 4 5 6 7 8 9 
#무한루프탈출

# for에서 break 사용하기
for i in range(10000) : 
    print(i, end = " ")
    if i == 10 :
        break
print(end="\n")
print("반복문 탈출")
#0 1 2 3 4 5 6 7 8 9 10 
#반복문 탈출

# while 반복문에서 continue로 코드실행 건너뛰기
i = 0
while i < 10: 
    i += 1
    if i % 2 == 0:
     continue # 아래 코드를 실행하지 않고 건너뜀
    print(i, end=" ")
#1 3 5 7 9

# for 반복문에서 continue로 코드실행 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue # 아래 코드를 실행하지 않고 건너뜀
    print(i, end=" ")
#1 3 5 7 9 

# for, while의 반복할 코드에서는 아무 일도 하지 않지만, 반복문의 형태는 유지하고 싶을 때 pass를 사용
# 나중에 작성해야 할 코드를 표시하는 용도
for i in range(10): 
    pass # 아무 일도 하지 않음
while True:
    pass # 무한루프 종료하려면 Ctrl+C

# 중첩 반복문
# 반복문 안에 반복문이 들어가는 형태

# for i in range(횟수) :
#     for j in range(횟수) :
#         안쪽 루프 반복구문
#         안쪽 루프 반복구문
#     바깥쪽 루프 반복구문       
for i in range(3):
    for j in range(2):
        print(j, end=' ')
    print()          # 다음 줄로 넘어감
#0 1
#0 1
#0 1

for i in range(3):
    for j in range(2):
        print("*")

for i in range(3):
    for j in range(2):
        print("*")
    print()          # 다음 줄로 넘어감

for i in range(10):
    for j in range(10):
        print("*", end ="")
print()          # 다음 줄로 넘어감

# 사각형 모양 출력하기
for i in range(3):
    for j in range(5):
        print('*', end='')
    print()

# 다음과 같이 가로와 세로를 입력 받아 직사각형을 그리는 프로그램을 작성하세요.
w = int(input("가로: "))
h = int(input("세로: "))

for i in range(h) :
    for j in range(w) :
        print('*', end='')
    print()

# 다음과 같이 층수를 입력 받아 아래와 같은 직각삼각형을 그리는 프로그램을 작성하세요.
# 층수: 5
# *
# **
# ***
# ****
# *****

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