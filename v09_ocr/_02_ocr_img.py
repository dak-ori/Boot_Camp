# pip install pytesseract
# pip install pillow

import pytesseract # 이미지에서 글자를 읽어내는 OCR 라이브러리
from PIL import Image # 이미지를 읽기 위한 도구

# Tesseract OCR 엔진의 실행 파일 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# C 드라이브 => Program Files => Tesseract-OCR

# 이미지 파일 열기
image = Image.open("v09_ocr/testocr.png")
# github에 링크 접속 후 사진을 OCR 폴더에 저장

# 이미지에서 한글 글자 인식
results = pytesseract.image_to_string(image, lang='eng')

# 결과 출력
print(results)
# The quick brown dog jumped over the
# lazy fox. The quick brown dog jumped
# over the lazy fox. The quick brown dog
# jumped over the lazy fox. The quick
# brown dog jumped over the lazy fox.