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

