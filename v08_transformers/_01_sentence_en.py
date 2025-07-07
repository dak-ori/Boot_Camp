# pip install sentence-transformers
# 문장 간 의미 유사도 측정을 위한 라이브러리
from sentence_transformers import SentenceTransformer, util

# 1. 사전 학습된 모델 로드
model = SentenceTransformer("all-MiniLM-L6-v2")
# => 가벼운 모델 중 하나, 영어 문장 기반

# # 2. 두 문장 입력
# sen1 = "I went to the library to read a book."
# sen2 = "I visited the libraty to read some books."

sen1 = "The cat is sleeping on the sofa"
sen2 = "Tomorrow, I have a math exam at school"
# 두 문장의 유사도 : 0.0208

# 3. 두 문장을 벡터로 변환
emb1 = model.encode(sen1, convert_to_tensor=True)
emb2 = model.encode(sen2, convert_to_tensor=True)

# 4. 코사인 유사도 계산
cos_sim = util.pytorch_cos_sim(emb1, emb2)
# => 코사인 값 범위 : -1 ~ 1
# => 의미 중심의 유사도를 잘 반영해줌

# 5. 결과 출력
# print(f"{cos_sim}")
# print(f"{cos_sim.item()}")
print(f"두 문장의 유사도 : {cos_sim.item():.4f}")
# tensor([[0.6860]])
# 0.686010479927063
# 0.6860