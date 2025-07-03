from ultralytics import YOLO
import cv2

# 비디오 주소
capture = cv2.VideoCapture('static/distance.mp4')

# 모델 선언
model = YOLO('models/yolo11n.pt')

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('비디오 확인')
        break
    
    # 객체 추적
    results = model.track(frame, persist = True)
    annotated_frame = results[0].plot()
    
    # 영상 출력
    resize_frame = cv2.resize(annotated_frame, (800,600))
    cv2.imshow('Tracking', resize_frame)
    
    # 영상 정지
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break