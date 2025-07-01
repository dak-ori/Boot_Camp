from termcolor import colored

def bold_string():
    '''
    출력할 문자의 굵기를 정하는 함수
    '''
    try:
        bold_value = int(input("문자를 굵게 한다 (0 or 1) > "))
        return bold_value
    except ValueError:
        return -1

def paint(sentence, color, bgcolor, bold):
    '''
    문장, 글자색, 배경색을 입력시 색을 교체하는 함수
    '''
    try:
        if bold == 1:
            return colored(sentence, color, 'on_'+bgcolor, attrs=['bold'])
        else:
            return colored(sentence, color, 'on_'+bgcolor)
    except Exception:
        print("잘못된 입력입니다.")

bold = bold_string()

if bold not in (0, 1):
    print("잘못된 입력입니다.")
else:
    try:
        sentence, color, bgcolor = input('문장, 글자색, 배경색을 순서대로 입력 > ').split()
        result = paint(sentence, color, bgcolor, bold)
        if result is not None:
            print(result)
    except Exception:
        print("잘못된 입력입니다.")