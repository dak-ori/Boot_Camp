from ultralytics import solutions
import cv2

# 비디오 주소
capture = cv2.VideoCapture('static/distance2.mp4')

# 모델 선언
distance_cal = solutions.DistanceCalculation(
    model = 'models/yolo11n.pt',
    show = True,
)

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 오류 처리
    if not success:
        print('비디오 확인')
        break
    
    # 모델 예측
    results = distance_cal(frame)

capture.release()
cv2.destroyAllWindows()