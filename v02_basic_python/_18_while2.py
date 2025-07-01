# kg -> b

def kg_to_pound(kg : float):
    pound = kg * 2.20462
    return pound

while True :
    try:
        input_kg = float(input(' > '))
        pound = kg_to_pound(input_kg)
        print(f'{input_kg:0.2f}kg -> {pound:0.2f}b')
        break
        
    except ValueError:
        print('잘못된 값 입력')