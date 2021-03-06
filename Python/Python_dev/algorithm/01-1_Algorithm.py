# 클래스명 camelCase
# 함수명 snake_case

# 알고리즘이란?

# 세 정수의 최댓값 구하기

# 순차 구조 (Sequential Structure)



print("세 정수의 최댓값을 구합니다.")

a = int(input("정수 a의 값을 입력하세요: "))
b = int(input("정수 b의 값을 입력하세요: "))
c = int(input("정수 c의 값을 입력하세요: "))

maximum = a 

# 선택 구조
if b > maximum :
    maximum = b

if c > maximum:
    maximum = c

print(f'최댓값은 {maximum}입니다.')


# 세 정수의 최댓값 구하기 (올바른 방식)



def max(a,b,c):

    maximum = a
    if b > maximum : maximum = b
    if c > maximum : maximum = c
    return maximum

print(f'max(3,2,1) = {max(3,2,1)}')


# 세 정수의 대소 관계와 중앙값
# 중앙값 : 주어진 값의 크기 순서대로 정렬했을 때 가장 중앙에 위치하는 값



def med(a,b,c):
    # 5 4 3 
    if a>=b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

a = int(input('정수 a의 값을 입력하세요: '))
b = int(input('정수 b의 값을 입력하세요: '))
c = int(input('정수 c의 값을 입력하세요: '))

print(f'중앙값은 {med(a,b,c)}입니다.')


# 세 정수를 입력받아 중앙값 구하기 2



def med2(a,b,c):

    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c


"""
중앙값을 구하는 첫번째 코드보다 비효율적

if(b >= a) , if(b <= a) 를 비교 후
elif 에서 다시 한번 (a > b) , (a < b)를 비교한다.

a와 b의 비교를 이미 마친 상태에서 다시 비교하는 것이 비효율적
"""    

# 조건문과 분기

# 입력받은 정숫값의 부호(양수, 음수, 0)을 판단하여 출력하는 프로그램


n = int(input('정수를 입력하세요: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')

# 연산자와 피연산자
"""
+ , - 등의 기호를 산술 연산자(Operator)
연산 대상을 피연산자(Operand)

단항 연산자 : 피연산자 1개 : -a
이항 연산자 : 피연산자 2개 : a < b
삼항 연산자 : 피연산자 3개 : a if b else c

이 중에서 조건 연산자인 if~else 문은 파이썬의 유일한 삼항 연산자

a = x if x > y else y
x와 y 중 큰 값을 a에 대입

"""

# 1부터 n까지 정수의 합 구하기 (while)

n = int(input('n값을 입력하세요'))

sum = 0 
i = 1 # count 변수

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


# 1부터 n까지 정수의 합 구하기 (for)



n = int(input('n값을 입력하세요: '))

sum = 0
# Count 변수 i는 1부터 시작하고 n + 1 이 될때까지 반복한다. 
# range(count 시작값 , count 종료값)
# count 시작값이 1 이기 때문에 종료값에 +1을 하는 것
for i in range(1, n + 1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')



# 가우스 덧셈으로도 1부터 n까지 정수의 합을 구할 수 있다.

sum = n * (n+1) // 2

12 // 2 == 6
12 % 2 == 0


# range() 함수로 이터러블 객체 생성하기

"""
range(n) : 0 이상 n 미만인 수를 차례로 나열하는 수열
range(a, b) : a 이상 b 미만인 수를 차례로 나열하는 수열
range(a, b, step) : a 이상 b 미만인 수를 step 간격으로 나열하는 수열

이터러블 객체는 반복할 수 있는 객체를 말하며
대표적인 이터러블 자료형으로 list, str, tuple이 있습니다.
"""

# 연속하는 정수의 합을 구하기 위해 값 정렬하기



a = int(input('정수 a를 입력하세요: '))
b = int(input('정수 b를 입력하세요: '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a, b+1): # a를 1 b를 2라고 할 시 2번 반복
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')



# 반복 과정에서 조건 판단하기 1

# a 부터 b까지 정수의 합 구하기 1




a = int(input('정수 a를 입력하세요. :'))
b = int(input('정수 b를 입력하세요. : '))

if a > b: # a와 b를 오름차순으로 정렬
    a, b = b, a

sum = 0 
for i in range(a , b+1):
    if i < b: # i가 b보다 작으면 합을 구하는 과정 출력
        print(f'{i}+ ', end='')
    else: # i가 b보다 크거나 같으면 최종값 출력을 위해 i = 를 출력
        print(f'{i} = ', end= '')
    sum += i

print(sum)


"""
ex) 3+4+5+6+7 =25 이면

더하는 수는 5개이고 + 기호는 4개

즉 , 더하는 수는 n개이면 + 기호는 n -1 개

하지만 위의 실습은 효율적이지 못함, 

a가 1이고 b가 100이라고 가정했을 시, for문에서 100번 반복하는 동안

1 ~ 99번은 i < b가 참 때문에 print(f'{i}+ ', end='') 식은 99번 실행하는 동안

print(f'{i} = ', end= '')식은 1번 실행

이럴 때는 for문 안에 있는 if 문을 제외하여 별도로 두는 것이 좋음

"""



# a 부터 b까지 정수의 합 구하기 2 (개선)

a = int(input('정수 a를 입력하세요. :'))
b = int(input('정수 b를 입력하세요. : '))

if a > b: # a와 b를 오름차순으로 정렬
    a, b = b, a

sum = 0

for i in range(a,b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)


"""
a = 3 , b = 5 입력

3(a값) + 4 + 5(b값) = 12(지금까지 더해진 i 값에 b 값을 더한 sum 값)

"""

# 반복 과정에서 조건 판단하기 2

# +와 -를 번갈아 출력하기



n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2:
        print('-',end='')
    else:
        print('+',end='')

print()


"""
위 실습 문제의 문제점 : 1. for문을 반복할 때마다 if문 수행
즉, n이 50,000이라면 if 문도 50,000번 실행

"""

n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2): # for 문을 순환하며 반환하는 값(인덱스)를 사용할 필요가 없기 때문에 _ 표시
    print('+-', end='') # +-를 n // 2개 출력

if n % 2: # n 값이 만약에 짝수이면 자동으로 if 조건이 0으로 되어 거짓이 된다.
    print('+', end='') # n이 홀수일 때만 +를 출력

print()


"""
위 실습 코드는 

카운트용 변수를 0에서 1로 변경해도 유연하게 변경할 수 있다.
range() 함수의 인수만 수정하면 된다.

for _ in range(1, n //2 + 1)
    print('+-', end='')

"""

# 반복 과정에서 조건 판단하기 3 
# * n개를 출력하되 w개마다 줄바꿈을 하는 프로그램

a = int(input('몇번 *를 출력하시겠습니까? : '))
b = int(input('몇번 줄바꿈을 하시겠습니까? : '))

for i in range(a): # a =3 이라고 했을 시 range를 (1,a+1) or ({0 생략},a) 으로 해야 3번 반복
    print('*',end='')
    if i % b == b - 1: # 1.
        print() # 줄바꿈

if a % b: # 2. 
    print() # 줄바꿈

"""
위의 실습 코드 설명
1. b가 5이면 a가 4,9,14일 때 줄바꿈 합니다.
a이 b의 배수이면 마지막 *을 출력한 다음 줄바꿈합니다. 
하지만 a가 b의 배수가 아니면 줄바꿈을 for문 밖에서 따로 수행해야 합니다.

하지만 위의 실습 코드도 for문을 반복할 때마다 if문을 실행하므로 효율적이지 않습니다.

"""

n = int(input('몇 개를 출력할까요?. : '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for _ in range(n // w): # n // w번 반복 [1]
    print('*' * w)

rest = n % w # [2] 
if rest: # n이 w의 배수 일 시 rest == 0 이므로 실행되지 않음
    print('*' * rest)

"""
[1] * 를 n // w번 출력하기

ex) n = 15 , w = 5 이면 *****를 3번 출력하고
n이 14, w 가 5이면 *****를 2번 출력합니다.

즉, n이 w의 배수이면 [1]에서 모든 출력이 완료됩니다. 

[2] * 를 n % w 번 출력 후 줄바꿈하기
n이 w의 배수가 아닌 경우 마지막 행을 출력합니다. n을 w로 나눈 나머지를 rest에 저장하고
* 를 rest개 출력한 다음 줄바꿈합니다.

예를 들어 n이 14 , w가 5면 rest에는 4가 저장
n이 w의 배수면 rest는 0
즉, rest가 0이면 *와 줄바꿈을 하지 않음

"""

# 양수만 입력 받기

while True:
    n = int(input('input n data '))
    if n > 0:
        break # n이 0보다 커질 때 까지 반복
    
# while break 코드를 통해서 0 이하 값이면 n을 다시 입력 받도록 함

sum = 0
i = 1

for i in range(1 , n+1):
    sum += i
    i += 1
    
print(f'1~{n} sum = {sum}')


"""
보충 수업 1-10 for문이 종료된 이후 카운터용 변수 i값 살펴보기

while i <= n  --> 반복을 종료할 때는 i는 n + 1
for i in range(시작값, n + 1)  --> 반복을 종료할 때 i는 n
"""

# 직사각형 넓이로 변의 길이 구하기

# Practice 1-17

area = int(input('직사각형의 넓이를 입력하세요 : '))

for i in range(1 , area + 1): # 1부터 사각형의 넓이 계산
    if i * i > area: break
    if area % i : continue # area가 i로 나누어 떨어지지 않으면 == area % i 를 할 시 나머지가 생기면 약수가 아님 따라서 for 조건식으로 돌아감
    print(f'{i} x {area // i}')

# Practice 1-18 

# 10~ 99 사이의 난수 n개 생성하기 (13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요'))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.') # for에 대한 else 문으로 for 반복이 종료되면 출력
    

# 반복문 건너뛰기와 여러 범위 스캔하기

# Practice 1-19
"""
1~12 까지 8을 건너뛰고 출력하기 (비효율적 코드)
판단을 13번 진행
"""

for i in range(1,13):
    if i == 8:
        continue
    print(i,end=' ')
    
    
print()

# Practice 1-20
"""
1~12까지 8을 건너뛰고 출력하기 (효율적 코드)

[1,2,3,4,5,6,7] , [9,10,11,12] 연결
"""

for i in list(range(1,8))+ list(range(9,13)):
    print(i, end=' ')
print()


# 비교 연산자를 연속으로 사용하는 방법과 드모르간의 법칙

# Practice 1C-3

while True:
    no = int(input('값을 입력하세요'))
    if no >= 10 and no <= 99: # 두자리 양수만 입력 받음
    
        break

while True:
    no = int(input('값을 입력하세요'))

    if not(no < 10 or no > 99):
        break
    
# == if 10 <= no <= 99 : 
# if not(no <10 or no > 99):

"""
x and y 와 not(not x or not y) 는 같다.

x or y 와 not(not x and not y)는 같다.
"""    

# 구구단

# Practice 1-21

print('-' * 27)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i * j:3}', end='')
    print() 
print('-' * 27)

# 보충 수업 1-12 난수를 생성하는 random.randint() 함수 알아보기
# random.randint(a,b) a 이상 b 이하인 정수 가운데 무작위로 1개를 뽑아 반환

# 직각 이등변 삼각형으로 출력하기 

n = int(input('짧은 변의 길이를 입력하세요 : '))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()

# 실습 1-23
# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

n = int(input('짧은 변의 길이를 구하세요,'))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()
    

# 실습 1C-4

# 함수 내부, 외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1 # 전역 변수
def put_id():
    x = 1 # 지역 변수
    print(f'id(x) = {id(x)}')
    
print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')

put_id()

# 실습 1C-5 

