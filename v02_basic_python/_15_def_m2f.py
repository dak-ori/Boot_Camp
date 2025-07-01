# meter => feet

def meter_to_feet(meter: float):
    feet = meter * 3.28084
    return feet

    input_num = input("meter > ")
    output = meter_to_feet(float(input_num))
    print(f'{output:.2f}')
