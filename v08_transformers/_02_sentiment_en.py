# pip install transformers
# pip install datasets
# pip install torch
from transformers import pipeline

# 1. 감정 분석 파이프라인 생성
classifier = pipeline("sentiment-analysis")
# 영어 문장의 감정을 'POSITIVE' 또는 'NEGATIVE'로 분류

# 2. 감정 분석할 문장을 입력
results = classifier("I'm having a hard time today.")

# 3. 결과 출력
print(f"감정 분석 결과 : {results[0]['label']}")
print(f"감정 분석 결과 : {results[0]['score']:.4f}")
# [{'label': 'POSITIVE', 'score': 0.9998754262924194}]