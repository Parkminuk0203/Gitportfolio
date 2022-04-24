'''
#표준 출력
#print() 함수
print("가나다라")
#가나다라
print("Hello World")
#Hello World

#문자열 표시
#문자열 표시는 "",'' 둘 다 가능. 단 쌍이 맞아야 함
print("Hello")
#Hello
print('Hello')
#Hello
print('가나다')
#가나다

#print() 안에 ,를 사용하면 여러개 출력 가능
print(1,2,3)
#1 2 3
print("Hello", "Python")
#Hello Python

#sep
print(1,2,3, sep = ", ") #sep에 ,와 공백 지정
#1, 2, 3
print(1,2,3, sep = ",")  #sep에 ,만 지정 
#1,2,3
print("Hello", "Python", sep = "") #sep에 빈 문자열을 지정
#HelloPython
print("010", "1234", "5678", sep ="-") #sep에 = 지정
#010-1234-5678

#print() 함수는 기본적으로 출력 후 줄이 바뀜
print("Hello")
print("World")
print("Good")
print("Job")
#Hello
#World
#Good
#Job

#end 옵션
#문장 출력 후 마지막을 무엇을 쓰고 끝낼지 정할 수 있음
print("Hello", end = "")
print("World", end = "")
print("Good", end = "")
print("Job")
#HelloWorldGoodJob
print("Hello", end = " ")
print("World", end = " ")
print("Good", end = " ")
print("Job")
#Hello World Good Job

#줄 바꿈(개행) 문자 : \n
#\n를 문자열에 넣어 출력하면 다른 출력 없이 줄만 바뀌게 됨
print("1\n2\n3") #문자열 안에 \n을 넣어 사용
#1
#2
#3
print(1,2,3, sep ="\n")
#1
#2
#3

#제어문자
#\n : 다음 줄로 이동하며 개행
#\t : 탭 문자, 여러 칸을 띄움
#\\ : \ 문자 자체를 출력할 때는 \\를 두 번 사용

#세미클론
#한 줄에 여러 구문을 사용할 때 사용
print("1"); print("2")
#1
#2

#정수값 15와 37의 합을 계산하여, 그 값이 “52”를 표시하는 프로그램을 작성하세요.
print(15+37)
#52

#정수값 15로부터 37을 뺀 값을 계산하고 "15에서 37을 뺀 값은 -22입니다.” 라고 표시하는 프로그램을 작성하세요.
print("15에서 37을 뺀 값은", 15-37, "입니다.")
#15에서 37을 뺀 값은 -22 입니다.

#print() 함수는 1회만 사용해서 동서남북을 줄바꿈으로 실행
print("동\n서\n남\n북")
#동
#서
#남
#북

#아래와 같이 표시하는 프로그램을 작성하세요. 단 프로그램 중에 print() 함수는 1회만 사용합니다.
#여보세요
#안녕하세요

#그럼 이만.
print("여보세요\n안녕하세요\n\n그럼 이만.")
#여보세요
#안녕하세요

#그럼 이만.

#정수를 저장하는 변수에 75를 넣고, 그 값을 표시하는 프로그램을 작성세요.
no = 75
print("no의 값은", no, "입니다.")
#no의 값은 75 입니다.

#빈칸을 채워 아래와 같이 날짜와 시간이 출력되는 프로그램을 작성하세요.
#2021/10/31 11:29:42
year  = 2021
month = 10
day = 31
hour = 11
min = 29
second = 41

print(year, month, day, sep = "/", end = " ")
print(hour, min, second, sep = ":")

#input() 함수
#형식 : 변수 = input("출력한 문자열")
#문자열 부분이 출력, 사용자의 입력이 변수에 저장
#input() 함수의 괄호 안에 질문을 입력하면 프롬포트에 띄어 줌
#입력은 숫자열로 받으려면 int(), float() 사용
name = input("이름이 무엇인가요? ")
print("만나서 반갑습니다. " + name + "씨!")
age = input("몇 살인가요? ")
print("네, 그러면 당신은 " + age + " 살이시군요, " + name + "씨!")
#이름이 무엇인가요? 박민욱
#만나서 반갑습니다. 박민욱씨!
#몇 살인가요? 23
#네, 그러면 당신은 23 살이시군요, 박민욱씨!

#숫자를 그냥 입력하면
x = input("첫 번째 정수: ")
y = input("두 번째 정수: ")
sum = x + y
print("합은 ", sum)
#첫 번째 정수: 10
#두 번째 정수: 20
#합은  1020
'''
#아래와 같이 읽어 들인 정수값을 변수에 저장하고 그 값을 표시하는 프로그램을 작성하세요.
#no의 값을 입력해주세요 : 32
#no의 값은 32 입니다.

