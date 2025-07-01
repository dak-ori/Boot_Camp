class Bread():
    def __init__(self, name: str = 'bread', price: int = 0, *filling: str, shell: str = ''):
        self.name = name
        self.price = price
        self.filling = filling
        self.shell = shell

    def get_shell(self, shell: str):
        self.shell = shell
        return self.shell

    def get_filling(self, *filling: str):
        self.filling = filling
        return self.filling

    def choose_price(self, price):
        try:
            self.price = int(price)
        except ValueError:
            print("숫자를 입력해주세요.")
        return self.price

    def make_bread(self):
        print(f"{self.shell}(으)로 겉을 만들고 {', '.join(self.filling)}을(를) 넣어 {self.name}을 만듭니다. 가격: {self.price}원")

bakery = Bread(name="피자")
bakery.get_shell('밀가루')
bakery.get_filling('치즈', '토마토', '바질')
bakery.choose_price(12000)
bakery.make_bread()