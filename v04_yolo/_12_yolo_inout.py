from ultralytics import solutions
import cv2

# 비디오 주소
capture = cv2.VideoCapture('static/vehicles.mp4')

# 좌표 설정
count_points = [
    [(10, 330), (630, 330)],
    [(630, 50), (10, 50)]
]

# 모델 선언
counter = solutions.ObjectCounter(
    model = 'models/yolo11n.pt',
    show = True,
    region = count_points,
)

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('비디오 확인')
        break
    
    # 모델 예측
    re_frame = cv2.resize(frame, (640, 480))
    results = counter(re_frame)
    
    # 종료 버튼
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('종료합니다')
        break

capture.release()
cv2.destroyAllWindows()

