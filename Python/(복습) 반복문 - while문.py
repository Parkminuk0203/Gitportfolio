''''''
# 0 부터 9 까지 출력하기
i = 0
while i < 10 :
    print(i)
    i += 1

# 반복문을 사용하여 다음과 같이 출력하는 프로그램을 작성하세요.
# 1 번째 Hello World!!
# 2 번째 Hello World!!
# 3 번째 Hello World!!
# 4 번째 Hello World!!
# 5 번째 Hello World!!
# 6 번째 Hello World!!
# 7 번째 Hello World!!
i = 0
while i < 7 :
    print("Hello World")
    i += 1

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
dan = int(input("정수를 입력하세요 : "))
i = 1
while i <= 9 :
    gugudan = dan * i
    print(dan,"*",i,"=",gugudan)
    i += 1

# 다음과 같이 양의 정수를 하나 입력 받아, 1부터 그 값까지 카운트 업 하는 프로그램을 작성하세요.
# 양의 정수 입력: 12
# 1 2 3 4 5 6 7 8 9 10 11 12 
count = int(input("양의 정수 입력: "))
i = 1
while i <= count :
    print(i, end = " ")
    i += 1
    
# 다음과 같이 양의 정수를 하나 입력 받아, 그 값을 0까지 감소시키면서 카운트 다운하는 프로그램을 작성하세요.
# 양의 정수 입력: 11
# 11 10 9 8 7 6 5 4 3 2 1 0 
count = int(input("양의 정수 입력: "))
while 0 <= count :
    print(count, end = " ") 
    count -= 1

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 짝수를 오름차순으로 출력하는 프로그램을 작성하세요.
# 양의 정수 입력: 19
# 2 4 6 8 10 12 14 16 18
num = int(input("양의 정수 입력: "))
i = 2
while i <= num :
    print(i, end = " ")
    i += 2

# 다음과 같이 양의 정수를 하나 입력 받아, 그 값 이하의 2의 제곱수를 오름차순으로 출력하는 프로그램을 작성하세요.
# 양의 정수 입력: 19
# 2 4 8 16 
num = int(input("양의 정수 입력: "))
i = 2
while i <= num :
    print(i)
    i *= 2

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 3의 배수를 출력하는 프로그램을 작성하세요.
# 양의 정수 입력: 5
# 3
# 6
# 9
# 12
# 15
num = int(input("양의 정수 입력: "))
i = 0
cnt = 0
while cnt < num :
    i += 3
    cnt += 1
    print(i)

# 다음과 같이 양의 정수를 하나 입력 받아, 그 수 만큼 세로로 *을 출력하는 프로그램을 작성하세요.
# 양의 정수 입력: 5
# *
# *
# *
# *
# *
num = int(input("양의 정수 입력: "))
i = 0
while i < num :
    print("*")
    i += 1

# 다음과 같이 정수 두 개를 입력 받아, 둘 중 큰 수에서 작은 수 사이를 카운트 다운 하는 프로그램을 작성하세요.
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
if num1 > num2 :    # 정수1이 정수2보다 크면
    upper = num1    # 큰 수에 정수1를 대입
    lower = num2    # 작은 수에 정수2를 대입
else :              # 아니면
    upper = num2    # 큰 수에 정수2를 대입
    lower = num1    # 작은 수에 정수 1을 대입
i = upper           # i에 큰 수를 대입
while i >= lower :  # i가 작은 수보다 크거나 같을 때 동안
    print(i)        # i를 계속 출력하고
    i -= 1          # i를 1씩 빼라.