from ultralytics import YOLO
import cv2

# 경로 설정
capture = cv2.VideoCapture()

# 모델 선언
model = YOLO('models/yolo11n-pose.pt')

while capture.isOpened():
    success, frame = capture.read()
    
    # 오류 처리
    if not success:
        print('확인 부탁드립니다')
        break
    
    # 모델 예측
    results = model(frame)
    annotated_frame = results[0].plot()
    
    # 화면 구성
    cv2.namedWindow('YOLO_POSE', cv2.WINDOW_NORMAL)
    cv2.imshow('YOLO_POSE', annotated_frame)
    
    # 종료 버튼
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('종료합니다')
        break

capture.release()
cv2.destroyAllWindows()

# 보편적으로 사용되는 키포인트 개수는 '17'개