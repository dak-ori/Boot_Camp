from ultralytics import solutions

searcher = solutions.VisualAISearch(
    data="v04_yolo/clip_main/images",  # 이미지 폴더 경로
    index="v04_yolo/clip_main/index.faiss",   # faiss 인덱스 파일 경로
    device="cpu"
)

results = searcher('fishing')