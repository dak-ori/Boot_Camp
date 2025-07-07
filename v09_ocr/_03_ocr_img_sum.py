# pip install pytesseract
# pip install pillow
# 1. OCR 이미지 글자 OCR 출력
import pytesseract # 이미지에서 글자를 읽어내는 OCR 라이브러리
from PIL import Image # 이미지를 읽기 위한 도구
from transformers import pipeline

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

# 2. 출력된 글자 요약 (ENG)
# 1. 파이프라인 생성
summarizer = pipeline(
    "summarization",
    model='t5-small'
)

# print(summarizer)
# 2. 요약할 긴 문장 입력
summary = summarizer(results)
# => 모델이 문장 내용을 읽고 핵심만 뽑아 요약문 생성

# 요약문 가져오기
sum = summary[0]['summary_text']

# 요약문 출력
print(f"### 요약된 문장 : {sum} ### ")

# 3. 영어 => 한국 번역
from googletrans import Translator
def translate_eng_to_kr(sen):
    '''
    주어진 영어 텍스트를 한국어로 번역하는 함수
    '''
    translater = Translator() # 번역기 객체 생성
    translation = translater.translate(sen, dest='ko')
    translated_sen = translation.text
    
    return translated_sen
    
# 영어로 요약된 문장을 한국어로 번역해주세요!
kr_sum = translate_eng_to_kr(sum)
print(f"### 한국어로 번역하여 요약된 문장 : {kr_sum} ### ")
### 한국어로 번역하여 요약된 문장 : 이것은 OCR 코드를 테스트하기위한 12 개의 포인트 텍스트입니다.빠른 갈색 개가 게으른 여우를 뛰어 넘었습니다. ###