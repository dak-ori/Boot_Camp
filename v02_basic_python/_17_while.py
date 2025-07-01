# meter => feet

def meter_to_feet(meter: float):
    feet = meter * 3.28084
    return feet

while True:
    try:
        input_num = input("meter > ")
        output = meter_to_feet(float(input_num))
        print(f'{input_num}m => {output:.2f}ft')
        break
    except ValueError:
        print("잘못된 값 입력")

