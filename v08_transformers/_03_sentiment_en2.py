from transformers import pipeline

# 1. 감정 분석을 위한 파이프라인 생성
snetiment_analyzer = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# print(snetiment_analyzer)

# 2. 분석할 문장 목록
senetences = [
    "I don't like a bird.",
    "I like a bird.",
    "I really hate summer.",
    "I like a winter."
]

# 3. 각 문장에 대해 감정 분석 수행
for s in senetences:
    result = snetiment_analyzer(s)[0]
    
    # 4. 결과 출력
    print(f"분석할 문장 : {s}")
    print(f"감정 : {result['label']}")
    print(f"점수 : {result['score']:.5f}")
    print("### 출력 완료!!! ###")