# conda create -n py_blip python==3.11.3
# pip install -U transformers
# pip install pillow
# pip install torch

# 간단한 AI 처리 도구
# from transformers import pipeline
# 모델
from transformers import BlipProcessor, BlipForConditionalGeneration
# 이미지 관련 도구
from PIL import Image

# 파이프라인
# pipe = pipeline(
#     "image-to-text",
#     model="Salesforce/blip-image-captioning-base"
# )

# 이미지 로드
img_path = "v10_blip/blip.jpg"
img_path = Image.open(img_path).convert("RGB")

# 파이프라인
prosser = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 이미지 텐서 변환
inputs = prosser(img_path, return_tensors='pt')
# => 모델이 처리할 수 있도록 변환

# 이미지를 설명하는 문장 생성
out = model.generate(**inputs)
# => 모델이 이미지 내용을 요약한 문장 생성

# 사람이 읽을 수 있는 문장으로 디코딩
caption = prosser.decode(out[0])

print(f"이미지 캡션 : {caption}")