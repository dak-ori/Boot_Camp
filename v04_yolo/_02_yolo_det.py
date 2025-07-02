from ultralytics import YOLO

# 모델 선언
model = YOLO('models/yolo11n.pt')

# 모델 예측
results = model(
    'static/eagle2_video.mp4',
    save = True
)