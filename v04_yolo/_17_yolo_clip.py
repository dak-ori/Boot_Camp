from ultralytics import YOLOWorld
import cv2

capture = cv2.VideoCapture('static/bird.mp4')

# 모델 선언
model = YOLOWorld('models/yolov8s-world.pt')

# 텍스트 기반 추론
model.set_classes(['bird'])

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('비디오 확인')
        break
    
    # 모델 예측
    results = model.predict(frame)
    annotated_frame = results[0].plot()
    
    # 크기 재조정
    resize_frame = cv2.resize(annotated_frame, (600,800))
    cv2.imshow('YOLO_CLIP', resize_frame)
    
    # 종료 버튼
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('종료합니다')
        break

capture.release()
cv2.destroyAllWindows()