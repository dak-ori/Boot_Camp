from ultralytics import YOLO
import cv2

# 모델 선언
model = YOLO('models/yolo11n-cls.pt')

# 모델 예측
results = model(
    'static/eagle1.jpg'
)

# 결과 확인
result_image = results[0].plot()
cv2.imwrite("./result.jpg", result_image)