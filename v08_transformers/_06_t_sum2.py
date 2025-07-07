from transformers import pipeline

# 1. 파이프라인 생성
summarizer = pipeline(
    "summarization",
    model='t5-small'
)

# print(summarizer)
# 2. 요약할 긴 문장 입력
summary = summarizer(
    '''
    Paulo Coelho's masterpiece tells the mystical story of Santiago, an Andalusian shepherd boy who yearns to travel in search of a worldly treasure. His quest will lead him to riches far different-and far more satisfying-than he ever imagined. Santiago's journey teaches us about the essential wisdom of listening to our hearts, of recognizing opportunity and learning to read the omens strewn along life's path, and, most importantly, to follow our dreams.
    '''
)
# => 모델이 문장 내용을 읽고 핵심만 뽑아 요약문 생성

# 요약문 가져오기
sum = summary[0]['summary_text']

# 요약문 출력
print(f"### 요약된 문장 : {sum} ### ")
'''
요약된 문장 : Paulo Coelho's masterpiece tells the mystical story of a shepherd boy . his quest will lead him to riches far different-and far more satisfying-than he imagined.
'''

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
### 한국어로 번역하여 요약된 문장 : Paulo Coelho의 걸작은 목자 소년의 신비로운 이야기를 들려줍니다.그의 퀘스트는 그를 상상했던 것보다 훨씬 더 만족스럽고 훨씬 더 만족스러운 부를 이 끌 것입니다. ###