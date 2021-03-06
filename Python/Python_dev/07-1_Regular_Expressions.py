# 07 정규 표현식

"""
주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해 보자.

1. 전체 텍스트를 공백 문자로 나눈다(split).
2. 나뉜 단어가 주민등록번호 형식인지 조사한다.
3. 단어가 주민등록번호 형식이라면 뒷자리를 *로 변환한다.
4. 나뉜 단어를 다시 조립한다.
"""


# 정규 표현식을 쓰지 않을 경우

data = """
park 800905-1049118
kim  700905-1059119
"""

result= []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14  and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "******"
        word_result.append(word)
    result.append(" ".join(word_result))

print(result)
print("\n".join(result))


# 정규 표현식을 쓸 경우

import re


data1 = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-******",data1))

# 정규 표현식의 기초, 메타 문자
# . ^ $ * + ? { } [ ] \ | ( )

# 1 . 문자 클래스 [ ]

"""
[ ] 사이의 문자들과 매치

정규표현식 [abc] 라면 a,b,c 중 한 개의 문자와 매치

ex) a,before,dude가 정규식 [abc]와 어떻게 매치되는지 살펴보자.

* a 는 정규식과 일치하는 문자인 a가 있으므로 매치
* before 는 정규식과 일치하는 문자인 b가 있으므로 매치
* dude 정규식과 일치하는 문자인 a,b,c중 어느 하나도 포함하고 있지 않으므로 매치되지 않음

[]안의 두 문자 사이에 하이픈(-) 을 사용하면 두 문자 사이의 범위(From- To)를 의미한다. 
예를들어 , [a-c]는 [abc] 와 동일 [0-5]는 [012345]와 동일

[a-zA-Z] : 알파벳 모두
[0-9] : 숫자

문자 클래스 [ ] 안에는 어떤 문자나 메타 문자도 사용할 수 있지만 주의해야 할 메타 문자가 1가지 있다. 
'^' 문자 클래스 안에 ^ 메타 문자를 사용할 경우에는 반대(not)라는 의미를 같는다 
예를들어 [^0-9] 라는 정규 표현식은 숫자가 아닌 문자만 매치된다.

"""


# 자주 사용하는 문자 클래스

"""
\d : 숫자와 매치, [0-9]와 동일한 표현식이다.
\D : 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s : whitespace 문자와 매치 ,[ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S : whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w : 문자 + 숫자 와 매치 , [a-zA-Z0-9_] 와 동일한 표현식이다.
\W : 문자 + 숫자 가 아닌 문자와 매치 , [^a-zA-Z0-9_]
"""

# Dot(.) 

"""

정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.
% re.DOTALL 옵션을 주면 \n 문자와도 매치된다.

"""

# 정규 표현식 Method()

"""
Method	목적
match()	문자열의 처음부터 정규식과 매치되는지 조사한다.
search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
"""

# 정규식을 이용한 문자열 검색

import re

p = re.compile('[a-z]+')

m = p.match("python")
print(m.group())







