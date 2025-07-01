import pyfiglet
from termcolor import colored

def decorate_text(text : str, color : str):
    '''
    텍스트를 꾸미는 함수
    '''
    # 1. 폰트 수정
    fonts_sentence = pyfiglet.figlet_format(text)
    
    # 2. 색상 수정
    color_sentence = colored(fonts_sentence, color)
    
    return color_sentence

print(decorate_text('Coffee', 'magenta'))

# return 을 사용하는 이유
# 1. 함수 값을 밖으로 전달하거나 변수에 저장가능
# 2. 함수를 종료할 수 있음
# 3. 코드 가독성 향상
