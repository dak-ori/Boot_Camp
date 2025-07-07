from transformers import pipeline

# 1. 파이프라인 생성
generator = pipeline(
    "text-generation",
    model='gpt2'
)
# GPT-2 모델은 주어진 문장을 이어서 자연스럽게 생성하는 것에 특화됨

# 1-1. 텍스트 입력
answer = input("생성 문장을 입력해주세요 : ")

# 2. 텍스트 생성 실행
result = generator(
    answer,
    max_new_tokens=50, # 생성할 최대 문장 길이
    num_return_sequences=1, # 생성할 결과 문장 수
    truncation=True # 입력 토큰 제한 명시
)

# 결과 출력
print(result[0]["generated_text"])
# 첫 번째 생성된 문장의 generated_text의 값을 꺼내서 출력
# Once upon a time...
# A man
# Was on a journey
# To help him
# Find his way?
# The man
# Was on a journey
# To help him Find his way?
# The man
# Was on a journey