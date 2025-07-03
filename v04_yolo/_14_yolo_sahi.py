# from sahi.utils.file import download_from_url
# from sahi.utils.ultralytics import download_yolo11n_model

# Download test images
# download_from_url(
#     "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/small-vehicles1.jpeg",
#     "static/small-vehicles1.jpeg",
# )
# download_from_url(
#     "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/terrain2.png",
#     "static/terrain2.png",
# )

from sahi.predict import get_prediction
from sahi import AutoDetectionModel as ADM

# 모델 경로
model_path = 'models/yolo11n.pt'

# 모델 선언
detection_model = ADM.from_pretrained(
    model_type = 'ultralytics',
    model_path = model_path
    )

# 모델 예측
results = get_prediction("static/small-vehicles1.jpeg", detection_model)

# 결과 저장
results.export_visuals('runs/export_results')