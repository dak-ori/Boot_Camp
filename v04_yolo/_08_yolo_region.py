from ultralytics import solutions
import cv2

# 비디오 주소
capture = cv2.VideoCapture('http://210.99.70.120:1935/live/cctv028.stream/playlist.m3u8')

# 좌표 설정 
region_points = {
    "region" : [(73, 600), (60, 400), (300, 150), (400, 150)],
    # "region_2nd" : [(860, 0), (1920, 0), (860, 600), (0, 600)],
}

# 모델 구성 및 구역 생성
region = solutions.RegionCounter(
    model = 'models/yolo11n.pt',
    region = region_points,
    show = True,
)

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 오류 처리
    if not success:
        print('비디오 확인')
        break
    
    results = region(frame)
    
    # 종료 버튼
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('종료합니다')
        break

capture.release()
cv2.destroyAllWindows()