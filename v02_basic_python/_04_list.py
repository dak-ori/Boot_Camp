# 배열 선언
color : list = ['red', 'purple', 'blue']

# 값 변환 
color[-1] = 'yellow'
color[0], color[1] = color[1], color[0]

color.insert(3, 'green') 
color.append('black') # 리스트 끝에 추가

color.remove('green')
color.clear() # 초기화

numbers : list = [1,3,4,5,2]

# numbers.sort(reverse = True) # 기존은 오름차순 (reverse = True : 내림차순)
numbers.reverse()
color.extend(numbers) # 다른 리스트와 병합


# 값 출력
for item in color:
    print(item, end=' ')    
print(100 in numbers)
