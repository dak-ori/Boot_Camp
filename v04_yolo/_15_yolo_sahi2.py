from sahi.predict import get_sliced_prediction
from sahi import AutoDetectionModel

# 모델 경로
model_path = 'models/yolo11n.pt'

# 모델 선언
detect_model = AutoDetectionModel.from_pretrained(
    model_type = 'ultralytics',
    model_path = model_path,
    confidence_threshold = 0.5 # 신뢰도가 0.5 이상만 반환
    )

# 슬라이스 기반 객체 ㅊ탐지 설정
results = get_sliced_prediction(
    image = 'static/small-vehicles1.jpeg',
    detection_model = detect_model,
    
    # 슬라이스 크기가 작을수록 정확하고, 오래걸림
    slice_width = 10,          # 슬라이스 가로 크기 
    slice_height = 10,         # 슬라이스 세로 크기
    
    # 각 슬라이스가 겹치는 비율 
    overlap_width_ratio = 0.2,  
    overlap_height_ratio = 0.2,
    
    # 로그 출력 (0: 없음, 1: 간단한 정보, 2: 상세 출력)
    verbose = 2
)

# 에측 결과 저장 
results.export_visuals('runs/export_results')
