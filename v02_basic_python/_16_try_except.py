# meter => feet

def meter_to_feet(meter: float):
    feet = meter * 3.28084
    return feet

try:
    input_num = input("meter > ")
    output = meter_to_feet(float(input_num))
    print(f'{output:.2f}')
except ValueError:
    print("잘못된 값 입력")

