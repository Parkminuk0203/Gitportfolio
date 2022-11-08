# score = [100,80,95,90,70]
# print(score)
# [100, 80, 95, 90, 70]

# score = [100,80,95,90,70]
# print(score[0])
# 100
# print(score[4])
# 70

# a = []
# b = [1,2,3]
# c = ['abc','def','가나다']
# d = [3.14,55,'Hello']

# 요소 연산
# d = [3.14, 55, 'Hello']
# print(d[0] + d[1])

# 요소 연산 불가
# print(d[0] + d[2])

# score = [100,80,95,90,70]
# sum = score[0] + score[1] + score[2] + score[3] + score[4]
# print('성적합계:',sum)
# print('성적평균:',sum/len(score))

# score = [100, 80, 95, 90, 70]
# print(score[2:4])
# [95, 90]
# print(score[:2])
# [100, 80]
# print(score[2:])
# [95, 90, 70]
# print(score[-5:])
# [100, 80, 95, 90, 70]
# print(score[:-1])
# [100, 80, 95, 90]

# score = [100,80,95,90,70]
# score[2] = 50
# print(score)
# [100, 80, 50, 90, 70]

# 덧셈 연산자
# a = [101, 102, 103]
# b = [201, 202, 203]
# print(a+b)
# [101, 102, 103, 201, 202, 203]

# 곱셈 연산자
# a = [101, 102, 103]
# print(a*2)
# [101, 102, 103, 101, 102, 103]

# c = [10, 20, 30]
# d = [10, 20, 30, 40]
# e = [10, 20, 30]
# print(c == e)
# True
# print(c != d)
# True
# print(c > d)
# False
# print(c < d)
# True

# score = [100, 80, 95, 90, 70]
# print(len(score))
# 5

from re import A


score = [100, 80, 95, 90, 70]
# print(sum(score))
# # 435
# print(sum(score)/len(score))
# # 87.0

# print(max(score))
# # 100
# print(min(score))
# # 70

# a = range(1,5)
# print(a)
# # range(1, 5)
# b = list(range(1,5))
# print(b)
# # [1, 2, 3, 4]
# c = list('test')
# print(c)
# ['t', 'e', 's', 't']

# a = [1,2,3]
# a.append(40)
# print(a)
# [1, 2, 3, 40]

# a = []
# a.append(40)
# print(a)
# [40]

# a = [1,2,3]
# a.append([40,50])
# print(a)
# [1, 2, 3, [40, 50]]
# print(len(a))
# 4

# a = [1,2,3]
# a.extend([40,50])
# print(a)
# [1, 2, 3, 40, 50]
# print(len(a))
# 5

# a = [1,2,3]
# a.insert(2, 100)
# print(a)
# # [1, 2, 100, 3]
# print(len(a))
# # 4

# a = [1,2,3]
# a.insert(0,100)
# print(a)
# # [100, 1, 2, 3]
# a = [1,2,3]
# a.insert(len(a), 100)
# print(a)
# [1, 2, 3, 100]

# a = [1,2,3]
# a.remove(2)
# print(a)
# [1, 3]

# remove( 값 )
# 리스트에서 해당 값이 두 개 이상 있으면?? 

# a = [1,2,3,1]
# a.remove(1)
# print(a)
# [2, 3, 1]

# a = [1,2,3]
# a.pop(1)
# print(a)
# [1, 3]

# a = [1,2,3]
# print(a.pop())
# # 3
# a.pop() # 요소를 쓰지 않으면 마지막 값을 반환하고 삭제

# a = [1,2,3]
# del a[1]
# print(a)
# [1,3]

# # index (값)
# a = [1,2,3,4,1]
# print(a.index(2))
# # 1
# print(a.index(1))
# # 0

# count (값)
# 특정 값의 개수를 알려준다
# 없으면 0 반환
# a = [1,2,3,1]
# print(a.count(1))
# 2
# print(a.count(4))
# 0

# 리스트 순서 뒤집기
# a = [1,2,3,4]
# a.reverse()
# print(a)
# [4, 3, 2, 1]

# a = [1,3,2,4,5,6]
# a.sort()
# print(a)
# [1, 2, 3, 4, 5, 6]

# a = [1,3,2,4,5,6]
# a.sort(reverse=True)
# print(a)
# [6, 5, 4, 3, 2, 1]

# clear()
# 모든 요소 값 삭제
# a = [1,2,3]
# a.clear()
# print(a)
# []

# 깊은 복사
# a = [1,2,3]
# b = a.copy()
# print(b)
# [1, 2, 3]

# a = [1,2,3]
# b = a
# print(b)
# [1, 2, 3]

# a = [1,2,3]
# b = a
# b[0] = 100
# print(a)
# print(b)

# 다음 같이 크기 5인 리스트에 처음 요소부터 순서대로 0, 1, 2, 3, 4를 하나씩 추가하고, 다음과 같이 출력하는 프로그램을 작성하세요. (for문 사용)
# list = []
# for i in range(5) :
#     list.append(i)

# for i in range(5) :
#     print("list[%d] = %d" % (i, list[i]))

# list = []
# for i in range(5) :
#     list.append(5-i)

# for i in range(5) :
#     print("list[%d] = %d" % (i, list[i]))
# list[0] = 5
# list[1] = 4
# list[2] = 3
# list[3] = 2
# list[4] = 1

# list = []
# for i in range(11) :
#     list.append(i/10)
# for i in range(11) :
#     print("list[%d] = %.1f" % (i, list[i]))

# 리스트를 변수로 넣기
# a = [1,2,3,4,5]
# for i in a :
#     print(i)
# 1
# 2
# 3
# 4
# 5

# num = ['one','two','three','four']
# for value in enumerate(num) :
#     print(value)
# # (0, 'one')
# (1, 'two')
# (2, 'three')
# (3, 'four')

# enumerate( ) 함수
# 인덱스와 요소를 같이 출력하려면

# num = ['one', 'two', 'three', 'four']
# for index, value in enumerate(num) :
#     print(index, value)
# # 0 one
# # 1 two
# # 2 three
# # 3 four

# while문으로 요소 출력하려면 인덱스로 요소값을 하나씩 접근 해야함

# a = [1,2,3,4,5]
# i = 0
# while i < len(a) :
#     print(a[i])
#     i += 1

# score = [100, 80, 95, 90, 70]
# sum=0
# for i in score :
#     sum += i
# print('성적합계:',sum)
# print('성적평균:',sum/5)

# score = [100, 80, 95, 90, 70]
# sum = 0
# i = 0
# while i < len(score) :
#     sum = sum + score[i]
#     i += 1
# print('성적합계:',sum)
# print('성적평균:',sum/len(score))

# 5명의 성적을 입력 받고, 성적을 모두 출력하는 프로그램을 작성하세요. 
# 성적 입력: 100
# 성적 입력: 80
# 성적 입력: 95
# 성적 입력: 90
# 성적 입력: 70
# 1 번째 성적:  100
# 2 번째 성적:  80
# 3 번째 성적:  95
# 4 번째 성적:  90
# 5 번째 성적:  70

STUDENT = 5
score = []
for i in range(STUDENT) :
    value = int(input("성적 입력: "))
    score.append(value)

for i in range(STUDENT) :
    print(i+1, "번째 성적: ", score[i])
