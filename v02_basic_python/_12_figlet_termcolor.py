# pyfiglet + termcolor

import pyfiglet
from termcolor import colored

# 1. 폰트
font_sentence = pyfiglet.figlet_format("*")

# 2. 색상
color_sentence = colored(font_sentence, 'light_magenta')

# 3. 출력
print(color_sentence)