# 기본 형태 : lamada 매개변수 : 함수 내용

# def add (a : int = 3, b : int = 4):
#     return a + b

# #overriding
# plus = add(4,4)

add = lambda a,b : a + b
print(add(3,4))

divide = lambda c,d : c / d
try:
    divide(10,0)
except ZeroDivisionError:
    print('0으로 나눌 수 없음')