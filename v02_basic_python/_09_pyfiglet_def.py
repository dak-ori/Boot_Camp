# 함수화

import pyfiglet as pyf

def pyfiglet(sentence):
    '''
    함수 설명 : 입력된 문자를 pyfiglet으로 변환 후 출력
    '''
    return print(pyf.figlet_format(sentence))

sentence = input(' > ')

pyfiglet(sentence)

# 함수 설명을 확인하는 키워드 - help
help(pyfiglet)