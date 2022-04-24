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
