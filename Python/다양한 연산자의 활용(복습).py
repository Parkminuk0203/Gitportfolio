'''
print(7 / 4)
#1.75
print(7 // 4) # //는 몫의 값을 구하는거
#1
print(7 % 4) # % 나머지
#3
print(123 % 121123123132)
#123
print(3**3)
#27
print(5.5+1)
#6.5
print(4.3-2.7)
#1.5999999999999996 정밀도

num = int(input("정수 입력: "))
print("10을 더하면",num+10)
print("10을 빼면",num-10)
print("10을 곱하면",num*10)
print("10을 나누면",num/10)
print("10을 나눈 몫을 구하면",num//10)
print("10을 나눈 나머지를 구하면",num%10)

num = int(input("정수 입력: "))
print(num,"나누기 5의 몫은",num // 5)
print(num,"나누기 5의 나머지는",num % 5)

num1 = int(input("정수1 입력: "))
num2 = int(input("정수2 입력: "))
sum = num1 + num2
multiply = num1 * num2
print("이들의 합은", sum, "이고 곱은", multiply, "입니다.")

num = float(input("실수 입력: "))
print("입력한 실수는", num)

num = float(input("cm 입력: "))
#inch = num / 2.54
print("인치로 변환하면", num / 2.54 , "inch 입니다.")

a = int(input("num1 입력: "))
b = int(input("num2 입력: "))
c = int(input("num3 입력: "))
print("합계는", a + b + c, "이고 평균은", (a+b+c)/3, "입니다.")

num1 = int(input("num1 입력: "))
num2 = int(input("num2 입력: "))
num3 = int(input("num3 입력: "))
sum = num1 + num2 + num3
Average = (num1 + num2 + num3) / 3
print("합계는", sum, "이고 평균은", Average, "입니다.")

# 20121213
# 01234567
num = str(input("생년월일: "))
year = num[:4] # 0~3
month = num[4:6] # 4~5
day = num[6:] # 6~끝까지
print("출생일자:", year + "년" , month + "월" , day + "일")
#출생일자: 2012년 12월 13일

a = 10
a = a + 1
print(a)
#11

a = 10
a += 1   

num = 200
num -= 100 # num = num - 100  
print(num)
#100
num *= 20 # num = num * 20
print(num)
#2000
num /= 2
print(int(num))
#1000
'''
print(10 == 10 and 5 == 6)
#False
print(10 == 10 and 6 == 6)
#True

a = 100
b = 0
print(not a) # not은 항상 부울타입의 값을 부정한다.
#False
print(not b)
#True

year = int(input("연도 입력: "))
if  ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) : 
    print("윤년 입니다.")
else : 
    print("윤년이 아닙니다.")

year = int(input("연도 입력: "))
ans = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print("윤년 여부:", ans)




  



