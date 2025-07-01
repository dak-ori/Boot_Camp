# 클래스 : 설계도
# 객체 : 클래스로 만들어낸 제품
# 속성 : 클래스 안의 변수
# 생성자 : 객체를 만들 때 실행되는 함수
# 메서드 : 클래스 안의 함수
# 인스턴스 : 메모리에 살아있는 객체

# 객체 > 인스턴스 : 인스턴스는 객체 안에 포함되어 있음


# 클래스 선언
class World():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def hello(self):
        print(self.name, self.age)

# 객체 생성
earth = World('지훈', 23)

# 메서드 호출
earth.hello()
