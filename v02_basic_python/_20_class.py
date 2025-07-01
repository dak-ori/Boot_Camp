class Animal():
    '''
    동물 클래스
    '''
    def __init__(self, name:str, **age:int):
        self.name = name
        self.age = age.get('age', None)
    
    def hello(self):
        print(f'나는 {self.name} 입니다')
        if self.age !=None:
            print(f"나이는 {self.age}살 입니다.")

result = Animal('개구리', age = 10)

result.hello()