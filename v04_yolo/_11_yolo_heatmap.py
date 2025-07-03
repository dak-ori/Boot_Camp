from ultralytics import solutions
import cv2

# 비디오 주소
capture = cv2.VideoCapture('static/distance2.mp4')

# 모델 선언q
heatmap = solutions.Heatmap(
    model = 'models/yolo11n.pt',
    show = True,
    colormap = cv2.COLORMAP_WINTER
)

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('비디오 확인')
        break
    
    # 모델 예측
    results = heatmap(frame)
    
    # 종료 버튼
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print('종료합니다')
        break

capture.release()
cv2.destroyAllWindows()