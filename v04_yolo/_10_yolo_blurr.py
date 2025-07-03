from ultralytics import solutions
import cv2

# 비디오 주소
capture = cv2.VideoCapture()

# 모델 선언
blurrer = solutions.ObjectBlurrer(
    model = 'models/yolo11n.pt',
    show = True,
    blur_ratio = 0.5    # default = 0.5
)

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('비디오 확인')
        break
    
    # 모델 예측
    results = blurrer(frame)
    
    # 종료 버튼
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print('종료합니다')
        break

capture.release()
cv2.destroyAllWindows()