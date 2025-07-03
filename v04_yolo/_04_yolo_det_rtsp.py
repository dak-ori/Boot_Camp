from ultralytics import YOLO
import cv2

# 비디오 경로 설정
capture = cv2.VideoCapture("https://its-stream3.busan.go.kr:8443/rtplive/cctv_73.stream/playlist.m3u8")

# 모델 선언
model = YOLO('models/yolo11n.pt')

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('파일을 다시 확인하세요')
        break
    
    # 모델 예측
    results = model(frame)
    annotated_frame = results[0].plot()
    
    # 결과 출력
    cv2.namedWindow('YOLO', cv2.WINDOW_NORMAL)
    cv2.imshow('YOLO', annotated_frame)

    #종료 버튼
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('종료하겠습니다')
        break

capture.release()
cv2.destroyAllWindows()