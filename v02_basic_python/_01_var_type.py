# 변수 목록
number : int = 10
decimal_Number : float = 0.1
string : str = "String"
yes : True
no : False
dictionary : dict = {'Key':'Value'}
no_Duplicate_value : set = ()
tuples : tuple = ()
nothing = None
array : list = [number, decimal_Number, string, dictionary]

# 출력
for i in range(4):
    print(array[i])

print(f'number의 값 : {number}')
print(f'number의 타입 : {type(number)}')

print(isinstance(tuples, int))