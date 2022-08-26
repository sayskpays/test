# IndexError

# 리스트/문자열 수를 넘는 요소/글자를 선택 할때 발생

# TypeError

# 서로 다른 자료를 연산 시 발생

# ValueError

# 변환할 수 없는 것을 변환하고자 할 때 발생
# -> 1. 숫자가 아닌 것을 숫자로 변환하려고 할 때
# -> 2. 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때


data = ['별', 2, 'M', 'Y']
str_data = """이름 : {}
나이: {}
성별: {}
지역: {}""".format(*data)
print(str_data)

