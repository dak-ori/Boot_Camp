from ultralytics import YOLO

# 모델 선언
model = YOLO('models/yolo11n.pt')

# 모델 예측
results = model(
    'static/people1.jpg',  # 사진 주소
    save = True,           # 자동 저장
    # conf = 0.5,          # 임계치 설정 / 높을수록 정확도 상승
    # save_text = True,    # 결과 정보 저장 여부 (객체 좌표)
    # save_conf = True,    # 객체의 대한 점수
    # save_crop = True,    # 각 객체에 대한 사진
    # max_dat = 5,         # 최대 객체 수
    classes=[73]           # 원하는 객체만 탐지
)

# print(model.names) # 객체 인덱스 확인