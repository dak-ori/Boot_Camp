# 제어문

# None, 0, 빈 문자열, 빈 데이터 구조는 False로 취급
# False로 취급하지 않는 모든 값

import random, os

num = int(input('1부터 6까지의 수 중 하나를 입력하시오 > '))
if random.randint(1,7) == num:
    print('Safe')
else:
    print('Fail')
    # os.remove('system32')