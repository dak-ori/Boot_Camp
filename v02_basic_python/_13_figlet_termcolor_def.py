# pyfiglet + termcolor => 함수

import pyfiglet
from termcolor import colored

def decorate_text():
    '''
    텍스트를 꾸미는 함수
    '''
    # 0. 텍스트 입력
    input_text = input(' > ')
    
    # 1. 폰트 수정
    fonts_sentence = pyfiglet.figlet_format(input_text)
    
    # 2. 색상 수정
    color_sentence = colored(fonts_sentence, 'light_blue')
    
    # 3. 출력
    print(color_sentence)

decorate_text()