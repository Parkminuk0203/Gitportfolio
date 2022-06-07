'''
# 리스트와 반복문
# 앞 챕터에서 봤던 것처럼 리스트를 사용하면 여러 데이터를 손쉽게 관리 할 수 있음. 
# 하지만 단순히 요소 하나하나를 따로 사용하기는 불편함
# -> 반복문과 같이 사용하면 아주 편리해짐

# for 반복문과 같이 사용
# for 반복문은 그냥 in뒤에 리스트를 지정
# 형식:
# for 변수 in  리스트 :
#     반복 문장
#     반복 문장
# 리스트 안의 요소들이 차례대로 변수에 대입되면서 반복 

# 요소 출력하기
# 리스트를 변수로 넣기
a = [1,2,3,4,5]
for i in a :
    print(i)
#1
#2
#3
#4
#5

# enumerate( ) 함수
# 리스트 요소에 순서 값을 부여해주는 함수
# 시퀀스 형(리스트, 튜플, 문자열 등)을 받으면 인덱스 값을 포함하는 enumerate 객체를 돌려 줌.
num = ['one','two','three','four']
for value in enumerate(num) :      
    print(value)
#(0, 'one')
#(1, 'two')
#(2, 'three')
#(3, 'four')

# 인덱스와 요소를 같이 출력하려면
num = ['one','two','three','four']
for index,value in enumerate(num) :
    print(index,value)
#0 one
#1 two
#2 three
#3 four

# while 반복문으로 요소 출력하기
# while문으로 요소 출력하려면 인덱스로 요소값을 하나씩 접근 해야함
a = [1,2,3,4,5]
i = 0
while i < len(a) :
    print(a[i])
    i += 1
#1
#2
#3
#4
#5

# 지난 챕터의 성적 리스트 처리 수정
score = [100, 80, 95, 90, 70]
sum=0
for i in score :
    sum += i
print('성적합계:',sum)
print('성적평균:',sum/5)



# 앞의 예제를 while문으로 변경
score = [100, 80, 95, 90, 70]
i = 0
sum = 0
while i < len(score) :
    sum += score[i]
    i += 1
print('성적합계:',sum)
print('성적평균:',sum / len(score))

# 5명의 성적을 입력 받고, 성적을 모두 출력하는 프로그램을 작성하세요
score = []
for i in range(5) :
    value = int(input("성적 입력: "))
    score.append(value)
for i in range(5) :
    print(i+1,"번째 성적:",score[i])

# 리스트에서 최소값 구하기
# 일반적인 최소값 알고리즘
# 1. 최소값 변수를 선언 
# 2. 리스트 첫번째 요소를 최소값이라 가정
# 3. 리스트의 다음 요소를 가져옴
# 4. 최소값 변수와 비교
# 5. 최소값 변수보다 작으면 
# -> 최소값 변수의 값을 비교한 값으로 바꿈
# 6. 끝날 때 까지 3번 부터 반복

score = [100, 80, 95, 90, 70]
min = score[0]   # 첫번째 요소를 최소값이라고 가정
for i in score :
    if i < min : # 비교 후 최소값 보다 작으면
        min = i  # 최소값 교체
print("최소값:", min)
#최소값: 70

# 리스트에서 최대값 구하기
# 반대로 최대값 구하기 구현
score = [100, 80, 95, 90, 70]
max = score[0]   # 첫번째 요소를 최대값이라고 가정
for i in score :
    if i > max : # 비교 후 최대값보다 i가 크면
        max = i  # max에 i값을 대입
print("최대값:", max)
#최대값: 100

score = [100, 80, 95, 90, 70]
max = score[0]   
min = score[0]
for i in score :
    if i > max : 
        max = i  
    elif i < min :
        min = i
print("최대값:",max,"최소값:",min)

# 정렬(sort)을 이용해도 최대, 최소값을 구할수 있다
# 오름차순 정렬 후 첫번째 요소 -> 최소값
# 내림차순 정렬 후 첫번째 요소 -> 최대값
score = [100, 80, 95, 90, 70]
score.sort()
min = score[0]
score.sort(reverse=True)
max = score[0]
print("최소값:", min)
print("최대값:", max)

# 파이썬에서 제공하는 min, max 함수 사용
score = [100,80,95,90,70]
min = min(score)
max = max(score)
print("최소값:",min)
print("최대값:",max)
#최소값: 70
#최대값: 100

# 요소의 합도 간단히
# sum( ) 함수를 사용할수 있음
score = [100, 80, 95, 90, 70]
sum = sum(score)
print("성적합계:", sum)
print("성적평균:", sum / len(score))
#성적합계: 435
#성적평균: 87.0

# 성적을 개수 제한없이 입력 받아 최고 점수, 최저점수, 평균을 구하는 프로그램을 작성하세요. 음수가 입력되면 종료되어 출력됩니다. (보초값)
# 종료하려면 음수를 입력하세요
# 성적 입력: 100
# 성적 입력: 90
# 성적 입력: 80
# 성적 입력: 70
# 성적 입력: 60
# 성적 입력: -1
# 최고 점수: 100
# 최저 점수: 60
# 평균 점수: 80.0

score = []
value = 0

print("종료하려면 음수를 입력하세요.")

while value >= 0 :
    value = int(input("성적 입력: "))
    if value >= 0 :
        score.append(value)

if len(score) > 0 :
    sum = sum(score)
    min = min(score)
    max = max(score)

    print("최고 점수:", max)
    print("최저 점수:", min)
    print("평균 점수:", sum / len(score))

# 리스트 함축(list comprehension)
# 리스트 안에 출력식과 for 반복문과 if 조건문을 사용하여 리스트를 생성하는 것
# 형식:
# [ 출력식  for 변수 in 리스트  if 조건식 ]
# if 조건식은 생략 가능

s = [ i*2 for i in range(10) ]
print(s)
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

list = [0,1,2,3,4,5]
s = [i for i in list]
print(s)
#[0, 1, 2, 3, 4, 5]

# 조건식 붙이기
# if를 사용하여 조건을 추가하여 출력할수 있다
s = [i for i in range(10) if i % 2 == 0]
print(s)
#[0, 2, 4, 6, 8]

s = [i**2 for i in range(10) if i % 2 == 0]
print(s)
#[0, 4, 16, 36, 64]

s = [(i+1)/10 for i in range(9)]
print(s)
#[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# 2차원 리스트
# 이제까지는 1차원 리스트를 사용함
# 2차원 리스트는 가로 x 세로 형태로 행(row), 열(column)
# 2차원 리스트 만들기
# 리스트 안에 리스트를 넣어서 만들수 있음
# 형식: 리스트 = [[요소, 요소], [요소, 요소], [요소, 요소]]
a = [[1, 2], [3, 4], [5, 6]]
print(a)
#[[1, 2], [3, 4], [5, 6]]

# 2차원 리스트의 요소에 접근하기
# 형식 : 리스트[세로인덱스][가로인덱스]
a = [[1, 2], 
    [3, 4], 
    [5, 6]]
print("a[0][0]:", a[0][0])
print("a[2][1]:", a[2][1])
a[1][0] = 100
print("a[1][0]:", a[1][0])
#a[0][0]: 1
#a[2][1]: 6
#a[1][0]: 100

# 2차원 리스트
# 반복문 사용하여 요소 출력하기
# for문 한 번 사용하기
a = [[1,2],[3,4],[5,6]]
for x, y in a :
    print(x,y)
#1 2
#3 4
#5 6

# 중첩 for문 사용하기
a = [[1,2],[3,4],[5,6]]
for i in a : # i 자리에 [1,2] 이런식으로 리스트 들어감
    for j in i : 
        print(j, end = ' ')
    print()
#1 2
#3 4
#5 6

# while문 한 번 사용하기
a = [[1,2],[3,4],[5,6]]
i = 0
while i < len(a) : # 반복할 때 리스트의 크기
    x, y = a[i]    # 요소 두 개를 한꺼번에 가져오기
    print(x, y)  
    i += 1         # 인덱스를 1 증가 시킴
#1 2
#3 4
#5 6

# pprint 모듈 사용하여 요소 출력하기
# 2차원 리스트를 가독성 좋게 출력
from pprint import pprint
a = [[1,2],[3,4],[5,6]]
pprint(a, indent=1, width=20)
#[[1, 2],
# [3, 4],
# [5, 6]]

# 반복문으로 2차원 리스트 만들기
# for 반복문을 사용
from pprint import pprint
a = []                              # 빈 리스트 생성
for i in range(3) :
    list = []                       # 안쪽 빈 리스트 생성
    for j in range(2) :
        list.append( i*2 + (j+1) )  # 안 리스트 요소 추가
    a.append(list)

pprint(a, indent=1, width=20)
#[[1, 2],
# [3, 4],
# [5, 6]]
'''
# 리스트의 함축으로 2차원 리스트 만들기
# 리스트의 함축 사용
from pprint import pprint
a = [[i*2 + (j+1) for j in range(2)] for i in range(3)]
pprint(a, indent=1, width=20)
#[[1, 2],
# [3, 4],
# [5, 6]]

# 학생의 이름과 성적을 2차원 리스트를 사용하여 저장하고 평균과 최고 성적 학생 이름과 점수를 출력하세요.
# john 80
# lan 95
# Alice 70
# 평균:  81.66666666666667
# 최고 성적 학생: Ian
# 최고 성적 점수: 95
students = [
['John', 80],
['Ian', 95],
['Alice', 70]
]
sum = 0
max_score = 0
for name, score in students:
    sum += score
    if(score > max_score):
        max_score = score
        max_name = name
print('평균: ', sum/len(students))
print('최고 성적 학생:', max_name)
print('최고 성적 점수:', max_score)